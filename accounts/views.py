from django.shortcuts import render, redirect
from .forms import CustomUserForm, ProfileUpdateForm
from .models import Profile
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data.get('user_type')
            user = form.save()
            user.profile.role = role
            user.save()
            
            group_name = role.capitalize()
            group, created = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)
            return redirect('login')
    else:
        form = CustomUserForm()
    return render(request, 'register.html', {'form': form})


# Profile update view for setting the publisher using the ProfileUpdateForm
@login_required
def profile_update(request):
    profile = Profile.objects.all()
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)        
            profile.save()
            return redirect("home")
    else:
        form = ProfileUpdateForm()
    return render(request, "update_publisher.html", {"form": form})
