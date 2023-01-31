from django.shortcuts import render, redirect, get_object_or_404
from .models import Datasekolah
from .forms import DatasekolahForm

# Create your views here.
def list_sekolah(request):
    list = Datasekolah.objects.all()
    return render(request, 'sekolah/list_sekolah.html', {'list': list})

def create_sekolah(request):
    if request.method == 'POST':
        form = DatasekolahForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sekolah')
    else:
        form = DatasekolahForm()
        return render(request, 'sekolah/create_sekolah.html', {'form': form})
    
def edit_sekolah(request, id):
    sekolah = Datasekolah.objects.get(id=id)
    if request.method == 'POST':
        form = DatasekolahForm(request.POST, instance=sekolah)
        if form.is_valid():
            form.save()
            return redirect('/sekolah')
    else:
        form = DatasekolahForm(instance=sekolah)
    return render(request, 'sekolah/edit_sekolah.html', {'form': form})

def delete_sekolah(request, id):
    del_sekolah = get_object_or_404(Datasekolah, id=id)
    del_sekolah.delete()
    return redirect(request.META.get('HTTP_REFERER', '/sekolah'))