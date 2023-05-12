from django.contrib.auth.models import Permission

from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from practice.serializers import UserSerializer, AccountSerializer, ProductSerializer, RegisterSerializer
from rest_framework import generics, viewsets, status
from practice.models import User, Product
from practice.custom_permission import is_permission


class UserDetailAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class CreateUser(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user_type = request.POST.get('user_type')
        role = request.POST.get('role')
        permissions = request.POST.getlist('permissions')

        if user_type == 3:
            user_obj = User.objects.filter(user_type=user_type).first()
            if user_obj:
                raise Exception('Client admin already exists')

        if is_permission(request.user, f'can_create_user_at_level{user_type}', role, permissions):
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            # raise Exception('You do not have permission to create user for this level')


# Create your views here.
class RetrieveUser(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        user_type = instance.user_type
        role = instance.role
        if is_permission(request.user, f'read_user_at_level{user_type}', role):
            serializer = self.get_serializer(instance)
            return Response(serializer.data)


class ListUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        if request.user.role:
            queryset = self.queryset.filter(user_type__gt=request.user.user_type, role=request.user.role)
        else:
            queryset = self.queryset.filter(user_type__gt=request.user.user_type)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        role = request.POST.get('role')
        permissions = request.POST.getlist('permissions')
        user_type = instance.user_type
        if is_permission(request.user, f'update_user_at_level{user_type}', role, permissions):

            user_type_from_request = request.data.get('user_type')
            user_permission = f'update_user_at_level{user_type_from_request}'

            if user_type_from_request and not user_permission in str(request.user.permissions.all()):
                raise Exception("you do not have permission to perform this action")

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        # return self.partial_update(request, *args, **kwargs)
        return Response(serializer.data)


class DeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        user_type = instance.user_type
        role = instance.role
        if is_permission(request.user, f'delete_user_at_level{user_type}', role):
            serializer = self.get_serializer(instance)
            instance.delete()
            return Response(serializer.data)


class AddRemovePermissions(APIView):
    serializer_class = UserSerializer

    def patch(self, request, pk):
        instance = User.objects.get(pk=pk)
        related_instance = Permission.objects.get(pk=request.permission)
        user_type = instance.user_type
        role = instance.role
        if is_permission(request.user, f'update_user_at_level{user_type}', role, request.permissions):
            if request.action == 'add':
                instance.permissions.add(related_instance)

            elif request.action == 'remove':
                instance.permissions.remove(related_instance)

            else:
                return Response({'error': 'Invalid action.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(instance)
        return Response(serializer.data)
