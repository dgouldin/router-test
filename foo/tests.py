from __future__ import absolute_import
from django.test import TestCase
from .models import Bar

class FooTest(TestCase):
    def test_bar(self):
        name = 'Bar'
        Bar.objects.create(name=name)
        assert Bar.objects.all()[0].name == name
