from django.shortcuts import render, redirect
from .models import Profile
from django.contrib import messages
import os
# Create your views here.
def insert(request):
    if request.method == "POST":
        name = request.POST['name']
        profile = request.FILES['profile']
        Profile.objects.create(
            name=name,
            profile=profile
        )
        messages.success(request, "Uploaded successfully!")
        return redirect('/')
    
def home(request):
    context = {
        'all_data': Profile.objects.all()
    }
    return render(request, 'index.html',context)

def edit(request, pk):
    data = Profile.objects.filter(id=pk)
    context = {
        'data':data
    }
    return render(request, 'edit.html', context)

def update(request, pk):
    update_data = Profile.objects.get(id=pk)
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(update_data.profile) > 0:
                os.remove(update_data.profile.path)
            update_data.profile = request.FILES['profile']
        update_data.name = request.POST['name']
        update_data.save()
        messages.success(request, "Data has been updated!")
        return redirect('/')
    
def delete(request, pk):
    get = Profile.objects.filter(id=pk)
    get.delete()
    messages.success(request, "Data has been deleted successfully!")
    return redirect('/')