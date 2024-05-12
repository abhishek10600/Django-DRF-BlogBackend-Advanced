# NOTE: has_permission() is used when we want to restrict the whole class.

# when we want only to allow the user that wrote the blog to update and delete the blog, then we use has_object_permission()

from rest_framework import permissions


# NOTE: If user is not admin or user is not logged in then just allow the GET request otherwise if the user is admin then allow all type of permission like POST, GET, PUT and DELETE.
# we inherit the IsAdminUser from permission because we want custom permission for the admin
class IsAdminUserOrReadOnly(permissions.BasePermission):  # custom permission

    # has_permission() is used when we want to restrict the whole class.
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # allow any body to perform GET operation
            return True
        else:  # only allow the admin user to perform GET, POST, PUT and DELETE operations.

            # it will return True if user is admin and it will return false if user is not admin
            return request.user and request.user.is_staff


# NOTE: If user is the creator of the object then only that user can update or delete that object. Others can only read that object.
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # allowing anybody to read the object data
            return True
        else:
            # checking if the user is the owner of the blog and if the user is owner then return True and if user not the owner return False.
            return obj.author == request.user
