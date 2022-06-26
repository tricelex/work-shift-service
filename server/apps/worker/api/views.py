from django.utils import timezone

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status



from server.apps.worker.models import Worker, WorkerShift

from .serializers import WorkerSerializer, WorkerShiftSerializer


class WorkerViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,GenericViewSet):
    """Worker viewset."""

    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()

    def get_queryset(self):
        return super().get_queryset()

class WorkerShiftViewSet(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,GenericViewSet):
    """Worker viewset."""

    serializer_class = WorkerShiftSerializer
    queryset = WorkerShift.objects.all()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    @action(detail=False)
    def today_shift(self, request):
        """
        Return the shift for the current day.
        """
        todays_date = timezone.localtime().date()

        today_workers = WorkerShift.objects.filter(process_date=todays_date)
        serializer = self.get_serializer(today_workers, many=True)
        return Response(serializer.data)
    

    def get_queryset(self):
        return super().get_queryset()