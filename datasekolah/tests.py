from django.test import TestCase
from django.contrib.auth.models import User
from .models import Datasekolah, StatusSekolah

class DatasekolahTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.sekolah = Datasekolah.objects.create(
            npsn='1234567890',
            nama='Sekolah Test',
            email='sekolah@test.com',
            hp='081234567890',
            alamat='Jl. Test 123',
            provinsi='Jawa Barat',
            kabupaten_kota='Bandung',
            kecamatan='Cibiru',
            status=StatusSekolah.SWASTA,
            created_by=self.user
        )

    def test_create_sekolah(self):
        sekolah = Datasekolah.objects.get(nama='Sekolah Test')
        self.assertEqual(sekolah.npsn, '1234567890')
        self.assertEqual(sekolah.email, 'sekolah@test.com')
        self.assertEqual(sekolah.hp, '081234567890')
        self.assertEqual(sekolah.alamat, 'Jl. Test 123')
        self.assertEqual(sekolah.provinsi, 'Jawa Barat')
        self.assertEqual(sekolah.kabupaten_kota, 'Bandung')
        self.assertEqual(sekolah.kecamatan, 'Cibiru')
        self.assertEqual(sekolah.status, StatusSekolah.SWASTA)
        self.assertEqual(sekolah.created_by, self.user)

    def test_update_sekolah(self):
        sekolah = Datasekolah.objects.get(nama='Sekolah Test')
        sekolah.nama = 'Sekolah Test Update'
        sekolah.save()
        sekolah = Datasekolah.objects.get(nama='Sekolah Test Update')
        self.assertEqual(sekolah.nama, 'Sekolah Test Update')

    def test_delete_sekolah(self):
        sekolah = Datasekolah.objects.get(nama='Sekolah Test')
        sekolah.delete()
        self.assertEqual(Datasekolah.objects.count(), 0)
