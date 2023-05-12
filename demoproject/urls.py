"""
URL configuration for demoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from practice.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()

router.register('user', UserDetailAPI)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('create_user/', CreateUser.as_view(), name='create_user'),
                  path('retrieve_user/<int:pk>', RetrieveUser.as_view(), name='retrieve_user'),
                  path('list_user/', ListUser.as_view(), name='list_user'),
                  path('update_user/<int:pk>', UpdateView.as_view(), name='update_user'),
                  path('delete_user/<int:pk>', DeleteView.as_view(), name='delete_user'),
                  path('', include(router.urls)),
              ] + router.urls
