from django.shortcuts import render
from .models import Datasekolah

# Create your views here.
def list_sekolah(request):
    list = Datasekolah.objects.all()
    return render(request, 'list_sekolah.html', {'list': list})