from django.test import TestCase
from datetime import date
from .models import Datasiswa, JenisKelamin

class DatasiswaTestCase(TestCase):
    def setUp(self):
        self.data = {
            'nama': 'John Doe',
            'email': 'johndoe@example.com',
            'hp': '081234567890',
            'alamat': 'Jl. Example No. 1',
            'jenis_kelamin': JenisKelamin.LAKILAKI,
            'tempat_lahir': 'Jakarta',
            'tanggal_lahir': date(2000, 1, 1),
            'nisn': '123456789'
        }

    def test_create_datasiswa(self):
        datasiswa = Datasiswa.objects.create(**self.data)
        self.assertIsInstance(datasiswa, Datasiswa)
        self.assertEqual(datasiswa.nama, self.data['nama'])
        self.assertEqual(datasiswa.email, self.data['email'])
        self.assertEqual(datasiswa.hp, self.data['hp'])
        self.assertEqual(datasiswa.alamat, self.data['alamat'])
        self.assertEqual(datasiswa.jenis_kelamin, self.data['jenis_kelamin'])
        self.assertEqual(datasiswa.tempat_lahir, self.data['tempat_lahir'])
        self.assertEqual(datasiswa.tanggal_lahir, self.data['tanggal_lahir'])
        self.assertEqual(datasiswa.nisn, self.data['nisn'])

    def test_update_datasiswa(self):
        datasiswa = Datasiswa.objects.create(**self.data)
        datasiswa.nama = 'Jane Doe'
        datasiswa.save()
        self.assertEqual(datasiswa.nama, 'Jane Doe')

    def test_delete_datasiswa(self):
        datasiswa = Datasiswa.objects.create(**self.data)
        datasiswa.delete()
        self.assertEqual(Datasiswa.objects.count(), 0)
