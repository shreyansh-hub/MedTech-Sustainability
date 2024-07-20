from django.shortcuts import render, get_object_or_404, redirect
from .models import HealthData
from .forms import HealthDataForm

def health_data_list(request):
    data = HealthData.objects.all()
    return render(request, 'ecohealth_app/health_data_list.html', {'data': data})

def health_data_detail(request, pk):
    data = get_object_or_404(HealthData, pk=pk)
    return render(request, 'ecohealth_app/health_data_detail.html', {'data': data})

def health_data_new(request):
    if request.method == "POST":
        form = HealthDataForm(request.POST)
        if form.is_valid():
            data = form.save()
            return redirect('health_data_detail', pk=data.pk)
    else:
        form = HealthDataForm()
    return render(request, 'ecohealth_app/health_data_edit.html', {'form': form})