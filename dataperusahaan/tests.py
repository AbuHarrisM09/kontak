from django.test import TestCase
from .models import Dataperusahaan
# Create your tests here.

class PerusahaanTestCase(TestCase):
    def setUp(self):
        #create test
        self.nama = Dataperusahaan.objects.create(nama="abu Harris")
        
    def test_create_dataperusahaan(self):
        new_dataperusahaan = Dataperusahaan.objects.create(
        nama=self.nama
    )