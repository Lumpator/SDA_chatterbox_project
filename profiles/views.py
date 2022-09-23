from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from profiles.models import Profile


# Create your views here.
@login_required
def profile_list(request):
    users = User.objects.all()
    profiles = Profile.objects.all()

    context = {"users": users, "profiles": profiles}

    return render(request, "profiles/users.html", context)

@login_required
def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)

    context = {"profile": profile}

    return render(request, "profiles/user.html", context)
