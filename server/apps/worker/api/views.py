
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from server.apps.worker.models import Worker

from .serializers import WorkerSerializer


class WorkerViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,GenericViewSet):
    """Worker viewset."""

    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()

    def get_queryset(self):
        return super().get_queryset()
