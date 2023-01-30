from django.test import TestCase
from .models import Dataperusahaan, JenisPerusahaan

class DataperusahaanModelTestCase(TestCase):
    def test_create_dataperusahaan(self):
        dataperusahaan = Dataperusahaan.objects.create(
            nama='Perusahaan X',
            email='perusahaanx@example.com',
            web='https://perusahaanx.com',
            hp='+62123456789',
            alamat='Jalan X No. Y, Kota Z',
            jenis_perusahaan=JenisPerusahaan.PT,
        )
        self.assertEqual(dataperusahaan.nama, 'Perusahaan X')
        self.assertEqual(dataperusahaan.email, 'perusahaanx@example.com')
        self.assertEqual(dataperusahaan.web, 'https://perusahaanx.com')
        self.assertEqual(dataperusahaan.hp, '+62123456789')
        self.assertEqual(dataperusahaan.alamat, 'Jalan X No. Y, Kota Z')
        self.assertEqual(dataperusahaan.jenis_perusahaan, JenisPerusahaan.PT)