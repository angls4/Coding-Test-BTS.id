from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.checklist import ChecklistViewSet, ChecklistItemViewSet

router = DefaultRouter()
router.register('checklist', ChecklistViewSet, basename='checklist')

urlpatterns = [
    path('', include(router.urls)),
    path('checklist/<int:checklist_id>/item', ChecklistItemViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('checklist/<int:checklist_id>/item/<int:pk>', ChecklistItemViewSet.as_view({'get': 'retrieve', 'delete': 'destroy','put': 'update_status'})),
    path('checklist/<int:checklist_id>/item/<int:pk>/rename', ChecklistItemViewSet.as_view({'put': 'rename'})),
]
