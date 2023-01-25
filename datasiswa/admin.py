from django.contrib import admin
from .models import Datasiswa

# Register your models here.
class DataSiswaAdmin(admin.ModelAdmin):
    list_display = [
        'nama',
        'nisn',
        'email',
        'hp',
        'alamat',
        'jenis_kelamin',
        'tempat_lahir',
        'tanggal_lahir',
    ]
admin.site.register(Datasiswa, DataSiswaAdmin)