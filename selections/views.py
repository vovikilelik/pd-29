from django.http import JsonResponse, HttpResponse

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from selections.models import Selection
from selections.serializers.selection_serializer import SelectionSerializer, SelectionDetailSerializer
from share.api.default_pagination_set import DefaultPaginationSet
from share.api.permissions import create_custom_action_permission, IsAuthenticatedOrAdmin
from users.models import User


class IsOwner(IsAuthenticatedOrAdmin):

    def has_object_permission(self, request, view, obj):
        if obj.owner_id == request.user.id:
            return True

        return request.user.role == User.ADMIN


class SelectionsViewSet(ModelViewSet):
    queryset = Selection.objects.all()

    serializer_class = SelectionSerializer
    pagination_class = DefaultPaginationSet
    permission_classes = [create_custom_action_permission(IsOwner, actions=['create', 'partial_update', 'update', 'destroy'])]

    def retrieve(self, request, *args, **kwargs):
        return JsonResponse(SelectionDetailSerializer(self.get_object()).data)

