
import uuid
from django.db import models

from server.apps.worker.utils.base_model import BaseAbstractModel

# Create your models here.

class Worker(BaseAbstractModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    


class WorkerShifted(BaseAbstractModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    worker = models.ForeignKey(Worker, on_delete=models.PROTECT())