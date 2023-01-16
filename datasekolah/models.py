from django.db import models

class JenisSekolah(models.TextChoices):
    SMK = 'SMK', ('Sekolah Menengah Kejuruan')
    UNIV = 'Universitas', ('Universitas')

# Create your models here.
class Datasekolah(models.Model):
    nama = models.CharField(max_length=50)
    alamat = models.TextField(blank=True, null=True)
    hp = models.CharField(max_length=13, blank=True, null=True)
    web = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    jenis_sekolah = models.CharField(
        max_length=20,
        choices=JenisSekolah.choices,
    )
    # created_by
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        db_table = "sekolah"
        ordering = ["-id"]
        verbose_name_plural = "Sekolah"