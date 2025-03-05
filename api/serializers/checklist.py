from rest_framework import serializers
from ..models.checklist import Checklist, ChecklistItem


class ChecklistItemSerializer(serializers.ModelSerializer):
    checklist = serializers.HiddenField(default=None)
    itemName = serializers.CharField(source='name')

    class Meta:
        model = ChecklistItem
        fields = ['itemName', 'checklist','completed']


class ChecklistSerializer(serializers.ModelSerializer):
    items = ChecklistItemSerializer(many=True, read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Checklist
        fields = "__all__"
