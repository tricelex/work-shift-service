
import uuid

from django.db import models

from server.apps.worker.utils.base_model import BaseAbstractModel


class Worker(BaseAbstractModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=12, blank=True)
    last_name = models.CharField(max_length=12, blank=True)
    email = models.EmailField(blank=True, db_index=True, max_length=254)
    
    def __str__(self) -> str:
        """Unicode representation for a Worker model."""
        return f'{str(self.id)} - {self.get_full_name()}'
    
    def get_full_name(self) -> str:
        """Return the first_name plus the last_name, with a space in between."""
        first_name = self.first_name
        last_name = self.last_name
        return f'{first_name} {last_name}'
        


class WorkerShift(BaseAbstractModel):
    FIRST_SHIFT = 0 
    SECOND_SHIFT = 1
    THIRD_SHIFT = 2
    
    SHIFT_TYPES = [
        (FIRST_SHIFT, '0 - 8'),
        (SECOND_SHIFT, '8 - 16'),
        (THIRD_SHIFT, '19 - 24'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    worker = models.ForeignKey(Worker, on_delete=models.PROTECT)
    shift = models.IntegerField(choices=SHIFT_TYPES, default=FIRST_SHIFT)
    process_date = models.DateField(db_index=True)

    
    def __str__(self) -> str:
        """Unicode representation for a WorkerShift model."""
        return f'{str(self.id)} - {self.worker.get_full_name()}'
