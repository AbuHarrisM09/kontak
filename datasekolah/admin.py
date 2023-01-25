from django.contrib import admin
from .models import Datasekolah

# Register your models here.
class DataSekolahAdmin(admin.ModelAdmin):
    list_display = [
        'npsn',
        'nama',
        'email',
        'hp',
        'alamat',
        'kecamatan',
        'kabupaten_kota',
        'provinsi',
        'status',
    ]

admin.site.register(Datasekolah, DataSekolahAdmin)