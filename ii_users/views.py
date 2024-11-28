from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def profile_view(request):
    profile = request.user.profile
    return render(request,'ii_users/profile.html', {"profile": profile})

@login_required
def edit_profile_view(request):
    
    form = ProfileForm(instance=request.user.profile)
    
    if (request.method == "POST"):
        form = ProfileForm(request.POST, request.FILES, instance = request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
        
    return render(request, "ii_users/edit_profile.html", {"form": form})