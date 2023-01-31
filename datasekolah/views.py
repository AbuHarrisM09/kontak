from django.shortcuts import render, redirect, get_object_or_404
from .models import Datasekolah
from .forms import DatasekolahForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def list_sekolah(request):
    list = Datasekolah.objects.all()
    return render(request, 'sekolah/list_sekolah.html', {'list': list})

@login_required
def create_sekolah(request):
    if request.method == 'POST':
        form = DatasekolahForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sekolah')
    else:
        form = DatasekolahForm()
        return render(request, 'sekolah/create_sekolah.html', {'form': form})

@login_required    
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

@login_required
def delete_sekolah(request, id):
    del_sekolah = get_object_or_404(Datasekolah, id=id)
    del_sekolah.delete()
    return redirect(request.META.get('HTTP_REFERER', '/sekolah'))