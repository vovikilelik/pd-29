from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.routers import SimpleRouter, Route
from rest_framework.viewsets import ModelViewSet, ViewSet

from share.api.default_pagination_set import DefaultPaginationSet
from users.models import User
from users.serializers.user_serializer import UserSerializer


# class UsersViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     pagination_class = DefaultPaginationSet
#


class UsersListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = DefaultPaginationSet


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroyView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UsersViewSet(ViewSet, UsersListView, UserDetailView, UserUpdateView, UserCreateView, UserDestroyView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = DefaultPaginationSet
