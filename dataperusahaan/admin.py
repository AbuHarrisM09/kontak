from django.contrib import admin
from .models import Dataperusahaan

# Register your models here.

class DataPerusahaanAdmin(admin.ModelAdmin):
    list_display = [
        'nama',
        'email',
        'web',
        'hp',
        'alamat',
        'jenis_perusahaan',
    ]

admin.site.register(Dataperusahaan, DataPerusahaanAdmin)