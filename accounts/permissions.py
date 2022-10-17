
from rest_framework import permissions
from django.contrib.auth.mixins import UserPassesTestMixin
from . import models




class OnlyAdminPermissionMixin():
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

class IsPresidentTestMixin(UserPassesTestMixin):
    def test_func(self):
        role = models.User.Role
        values = [role.MANAGER, role.PRESIDENT, role.SR_MANAGER]
        return self.request.user.role in values
    


class OnlyStaff(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

class OnlyStaffPermissionMixin():
    permission_classes = [permissions.IsAuthenticated, OnlyStaff]

class IsStaffTestMixin(UserPassesTestMixin):
    def test_func(self):
        role = models.User.Role
        values = [role.MANAGER, role.PRESIDENT, role.SR_MANAGER, role.STANDARD]
        return self.request.user.role in values