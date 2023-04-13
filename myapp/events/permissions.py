from rest_framework import permissions

class IsOrganizer(permissions.BasePermission):
    """
    Permission personnalisée permettant uniquement aux organisateurs de créer des événements
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_organizer
        
class IsAuthenticatedOrOrganizer(permissions.BasePermission):
    """
    Permission personnalisée permettant à tous les utilisateurs authentifiés d'accéder à la liste des événements,
    mais uniquement aux organisateurs de créer des événements.
    """

    def has_permission(self, request, view):
        if request.method == "GET":
            return request.user.is_authenticated
        else:
            return request.user.is_authenticated and request.user.is_organizer