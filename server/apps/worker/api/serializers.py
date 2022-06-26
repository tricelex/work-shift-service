from typing import Any
from django.utils import timezone


from rest_framework import serializers

from server.apps.worker.models import Worker, WorkerShift


class WorkerSerializer(serializers.ModelSerializer[Worker]):
    """Serializer for the Worker model."""

    class Meta(object):
        model = Worker
        fields = ['id', 'first_name', 'last_name', 'email']

class WorkerShiftSerializer(serializers.ModelSerializer[WorkerShift]):
    """Serializer for the WorkerShift model."""
    
    class Meta(object):
        model = WorkerShift
        fields = ['id', 'worker', 'shift', 'process_date']
    
    def create(self, validated_data: dict[str, Any]) -> Any:
        """Overridden method."""
        return WorkerShift.objects.create(**validated_data)
    
    def validate(self, attrs: dict[str, Any]) -> dict[str, Any]:
        """Check if this worker exists on process date."""
        todays_date = timezone.localtime().date()

        if (
            WorkerShift.objects.filter(process_date=todays_date, worker=attrs['worker']).exists()
        ):
            raise serializers.ValidationError({'worker': ['Worker already has shift for today.']})

        return attrs


    