from django.contrib.auth.models import AnonymousUser
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.routers import SimpleRouter, Route
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet

from share.api.default_pagination_set import DefaultPaginationSet
from share.api.permissions import create_custom_action_permission, IsAuthenticatedOrAdmin
from users.models import User, Location
from users.serializers.location_serializer import LocationSerializer
from users.serializers.user_serializer import UserSerializer


class IsOwner(IsAuthenticatedOrAdmin):

    def has_object_permission(self, request, view, obj):
        if obj.id == request.user.id:
            return True

        return request.user.role == User.ADMIN


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = DefaultPaginationSet
    # permission_classes = [create_custom_action_permission(IsOwner)]


class LogoutView(APIView):

    def get(self, request: Request):
        if isinstance(request.user, AnonymousUser):
            return Response(status=401)

        request.user.auth_token.delete()

        return Response(status=200)


class LocationsViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    pagination_class = DefaultPaginationSet
