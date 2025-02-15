"""Init."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Init."""

    class Meta:
        """Init."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
