from django.db import models


class BaseAbstractModel(models.Model):
    created_datetime = models.DateTimeField('Created at',auto_now_add=True)
    created_datetime = models.DateTimeField('Last updated at',auto_now=True)
    
    objects = models.Manager()
    
    class Meta:
        abstract = True