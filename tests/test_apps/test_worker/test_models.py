from factory.django import DjangoModelFactory
from django.test import TestCase

from server.apps.worker.models import Worker, WorkerShift


class WorkerFactory(DjangoModelFactory):
    first_name = 'Jon'
    last_name = 'Snow'
    
    class Meta(object):
        model = Worker
        django_get_or_create = ('email',)
        
        
class WorkerShiftFactory(DjangoModelFactory):
    class Meta(object):
        model = WorkerShift
        

class WorkerTests(TestCase):
    def test_unicode(self):
        """Tests unicode."""
        
        worker = WorkerFactory.create(email='test@example.com')
        
        self.assertEqual(str(worker), f'Jon Snow')
        
class WorkerShiftTests(TestCase):
    def test_unicode(self):
        """Tests unicode."""
        
        worker = WorkerFactory.create(email='test@example.com')
        worker_shift = WorkerShiftFactory.create(worker=worker)
        
        self.assertEqual(str(worker_shift), f'Jon Snow')