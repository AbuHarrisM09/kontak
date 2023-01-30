from django.shortcuts import render, redirect
from .models import Dataperusahaan
from .forms import DataperusahaanForm

# Create your views here.
def list_perusahaan(request):
    list = Dataperusahaan.objects.all()
    return render(request, 'perusahaan/list_perusahaan.html', {'list': list})

def create_perusahaan(request):
    if request.method == 'POST':
        form = DataperusahaanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/perusahaan')
    else:
        form = DataperusahaanForm()
        return render(request, 'perusahaan/create_perusahaan.html', {'form': form})

def edit_perusahaan(request, id):
    perusahaan = Dataperusahaan.objects.get(id=id)
    if request.method == 'POST':
        perusahaan.name = request.POST['name']
        perusahaan.description = request.POST['description']
        perusahaan.save()
        return redirect('index')
    return render(request, 'perusahaan/edit_perusahaan.html', {'item': perusahaan})