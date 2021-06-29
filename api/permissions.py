from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsAuthorOrReadOnly2(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.bill.user == request.user
