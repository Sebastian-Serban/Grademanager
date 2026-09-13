from rest_framework import serializers

from . import permissions
from .models import Subject
from .permissions import IsCreatorOrReadOnly


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model: Subject
        fields = ["id", "name", "grade", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]
        permission_classes = [IsCreatorOrReadOnly, permissions.IsCreatorOrReadOnly]
