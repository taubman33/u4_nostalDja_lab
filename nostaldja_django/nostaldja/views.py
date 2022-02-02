from django.shortcuts import render
from .forms import DecadeForm, FadForm

# Create your views here.


from .models import Decade, Fad


def decade_list(request):
    decades = Decade.objects.all()
    return render(request, 'nostaldja/decade_list.html', {'decades': decades})


def fad_list(request):
    fads = Fad.objects.all()
    return render(request, 'nostaldja/fad_list.html', {'fads': fads})


def decade_detail(request, pk):
    decade = Decade.objects.get(id=pk)
    return render(request, 'nostaldja/decade_detail.html', {'decade': decade})


def fad_detail(request, pk):
    fad = Fad.objects.get(id=pk)
    return render(request, 'nostaldja/fad_detail.html', {'fad': fad})


def decade_create(request):
    if request.method == 'POST':
        form = DecadeForm(request.POST)
        if form.is_valid():
            decade = form.save()
        return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm()
    return render(request, 'nostaldja/decade_form.html', {'form': form})

def fad_create(request):
    if request.method == 'POST':
        form = FadForm(request.POST)
        if form.is_valid():
            fad = form.save() 
            return redirect('fad_detail', pk=fad.pk)
    else:
        form = FadForm()
    return render(request, 'nostaldja/fad_form.html', {'form': form})


def decade_edit(request, pk):
    deacde = Decade.objects.get(pk=pk)
    if request.method == "POST":
        form = DecadeForm(request.POST, instance=decade)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', pk=decade.pk)
    else:
        form = DecadeForm(instance=decade)
    return render(request, 'nostaldja/decade_form.html', {'form': form})


def fad_edit(request, pk):
    fad = Song.objects.get(pk=pk)
    if request.method == "POST":
        form = FadForm(request.POST, instance=fad)
        if form.is_valid():
            fad = form.save()
        return redirect('fad_detail', pk=fad.pk)

    else:
        form = FadForm(instance=fad)
    return render(request, 'nostaldja/fad_form.html', {'form': form})

def decade_delete(request, pk):
    Decade.objects.get(id=pk).delete()
    return redirect('decade_list')

def fad_delete(request, pk):
    Fad.objects.get(id=pk).delete()
    return redirect('fad_list')
