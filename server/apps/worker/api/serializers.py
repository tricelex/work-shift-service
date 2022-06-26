from rest_framework import serializers

from server.apps.worker.models import Worker, WorkerShift


class WorkerSerializer(serializers.ModelSerializer):
    """Serializer for the Worker model."""

    class Meta(object):
        model = Worker

class WorkerShiftSerializer(serializers.ModelSerializer):
    """Serializer for the WorkerShift model."""

    class Meta(object):
        model = WorkerShift