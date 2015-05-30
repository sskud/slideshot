from django.http import Http404

from rest_framework import permissions

from broadcasts.models import Broadcasting, Slide

class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        #logic will be later
        return True