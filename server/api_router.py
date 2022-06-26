from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from server.apps.worker.api.views import WorkerViewSet, WorkerShiftViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('workers', WorkerViewSet)
router.register('workers_shift', WorkerShiftViewSet)


app_name = 'api'
urlpatterns = router.urls
