from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from ..models.checklist import Checklist, ChecklistItem
from ..serializers.checklist import ChecklistSerializer, ChecklistItemSerializer


class ChecklistViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ChecklistSerializer

    def get_queryset(self):
        return Checklist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ChecklistItemViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ChecklistItemSerializer

    def get_queryset(self):
        checklist_id = self.kwargs["checklist_id"]
        return ChecklistItem.objects.filter(
            checklist__id=checklist_id, checklist__user=self.request.user
        )

    def perform_create(self, serializer):
        checklist_id = self.kwargs["checklist_id"]
        checklist = get_object_or_404(
            Checklist, id=checklist_id, user=self.request.user
        )
        serializer.save(checklist=checklist)

    @action(detail=True, methods=["put"])
    def rename(self, request, checklist_id=None, pk=None):
        item = get_object_or_404(
            ChecklistItem,
            id=pk,
            checklist__id=checklist_id,
            checklist__user=request.user,
        )
        item.name = request.data.get("itemName", item.name)
        item.save()
        return Response(
            {"message": "Item renamed successfully"}, status=status.HTTP_200_OK
        )

    @action(detail=True, methods=["put"])
    def update_status(self, request, checklist_id=None, pk=None):
        item = get_object_or_404(
            ChecklistItem,
            id=pk,
            checklist__id=checklist_id,
            checklist__user=request.user,
        )
        item.completed = not item.completed
        item.save()
        return Response(
            {"message": "Item status updated successfully"}, status=status.HTTP_200_OK
        )
