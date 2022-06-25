from django.urls import path

from server.apps.worker.views import index

app_name = 'worker'

urlpatterns = [
    path('test/', index, name='test'),
]
