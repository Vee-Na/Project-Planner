from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):

    def has_permission(self, request, view):

        return bool(request.user and request.user.is_authenticated and request.user.role=='Admin') #is_authenticated is a method but here treated as an attribute

class IsDeveloper(BasePermission):

    def has_permission(self, request, view):

        return bool(request.user and request.user.is_authenticated and request.user.role=='Developer') 

class IsProjectCoordinator(BasePermission):

    def has_permission(self, request, view):

        return bool(request.user and request.user.is_authenticated and request.user.role=='Project Coordinator') 