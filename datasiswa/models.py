from django.db import models

class JenisKelamin(models.TextChoices):
    LAKILAKI = 'L', ('Laki-laki')
    PEREMPUAN = 'P', ('Perempuan')

# Create your models here.
class Datasiswa(models.Model):
    nama = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=True)
    hp = models.CharField(max_length=13, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    jenis_kelamin = models.CharField(
        max_length=1,
        choices=JenisKelamin.choices,
    )
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    nisn = models.CharField(max_length=20)
    # created_by
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        db_table = "siswa"
        ordering = ["-id"]
        verbose_name_plural = "Siswa"