# Create your tests here.
from django.test import TestCase
from .models import CV


class ModelTesting(TestCase):
    def setUp(self) -> None:
        self.CV = CV.objects.create(name="Shivansh")

    def test_cv_model(self):
        cv = self.CV
        self.assertTrue(isinstance(cv, CV))
        self.assertEqual(str(cv), "CV for Shivansh")
