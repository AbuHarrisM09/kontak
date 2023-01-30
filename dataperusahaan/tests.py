from django.test import TestCase
from .models import Dataperusahaan, JenisPerusahaan

class DataperusahaanTestCase(TestCase):
    def setUp(self):
        Dataperusahaan.objects.create(
            nama="Perusahaan A",
            email="perusahaan_a@example.com",
            jenis_perusahaan=JenisPerusahaan.PT
        )

    def test_create(self):
        perusahaan = Dataperusahaan.objects.get(nama="Perusahaan A")
        self.assertEqual(perusahaan.nama, "Perusahaan A")
        self.assertEqual(perusahaan.email, "perusahaan_a@example.com")
        self.assertEqual(perusahaan.jenis_perusahaan, "PT")

    def test_update(self):
        perusahaan = Dataperusahaan.objects.get(nama="Perusahaan A")
        perusahaan.nama = "Perusahaan B"
        perusahaan.save()

        updated_perusahaan = Dataperusahaan.objects.get(id=perusahaan.id)
        self.assertEqual(updated_perusahaan.nama, "Perusahaan B")

    def test_delete(self):
        perusahaan = Dataperusahaan.objects.get(nama="Perusahaan A")
        perusahaan.delete()

        with self.assertRaises(Dataperusahaan.DoesNotExist):
            Dataperusahaan.objects.get(id=perusahaan.id)
