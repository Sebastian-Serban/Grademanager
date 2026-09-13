from rest_framework import serializers

from .models import Grade


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ["id", "grade", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]
