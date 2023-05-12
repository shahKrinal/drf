from practice.models import User


def is_permission(user, user_permission, role=None, permissions=None):
    if user.is_superuser:
        return True
    else:
        if user_permission not in str(user.permissions.all()):
            raise Exception("you do not have permission to perform this action")
        if role and not role == user.role:
            raise Exception("you do not have permission to perform this action")
        perm1 = set(user.permissions.values_list('id', flat='true'))
        perm2 = set([] if permissions is
                          None else [int(val) for val in permissions])
        if perm1 and perm2 and not perm2.issubset(perm1):
            raise Exception("you do not have permission to assign this permission")

        return True
