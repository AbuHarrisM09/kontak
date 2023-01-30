from django.db import models


class JenisPerusahaan(models.TextChoices):
    PT              = 'PT', ('Perseroan Terbatas')
    CV              = 'CV', ('Commanditaire Vennootschap')
    KOPERASI        = 'Koperasi', ('Koperasi')
    FIRMA           = 'Firma', ('Firma')
    PERSERO         = 'Persero', ('Persero')
    PERSEORANGAN    = 'Perseorangan', ('Perseorangan')

# Create your models here.
class Dataperusahaan(models.Model):
    nama = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True, null=True)
    web = models.CharField(max_length=100, blank=True, null=True)
    hp = models.CharField(max_length=13, blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    jenis_perusahaan = models.CharField(
        max_length=20,
        choices=JenisPerusahaan.choices,
    )
    # created_by
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        db_table = "perusahaan"
        ordering = ["-id"]
        verbose_name_plural = "Perusahaan"