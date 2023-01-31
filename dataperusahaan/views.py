from django.shortcuts import render, redirect, get_object_or_404
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
        form = DataperusahaanForm(request.POST, instance=perusahaan)
        if form.is_valid():
            form.save()
            return redirect('/perusahaan')
    else:
        form = DataperusahaanForm(instance=perusahaan)
    return render(request, 'perusahaan/edit_perusahaan.html', {'form': form})

def delete_perusahaan(request, id):
    del_perusahaan = get_object_or_404(Dataperusahaan, id=id)
    del_perusahaan.delete()
    return redirect(request.META.get('HTTP_REFERER', '/perusahaan'))
