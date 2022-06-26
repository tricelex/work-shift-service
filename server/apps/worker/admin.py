from django.contrib import admin

from server.apps.worker.models import Worker, WorkerShift


@admin.register(Worker)
class BlogPostAdmin(admin.ModelAdmin[Worker]):
    """Admin panel example for ``Worker`` model."""
@admin.register(WorkerShift)
class BlogPostAdmin(admin.ModelAdmin[WorkerShift]):
    """Admin panel example for ``WorkerShift`` model."""
