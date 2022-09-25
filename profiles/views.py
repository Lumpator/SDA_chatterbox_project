from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404

from profiles.forms.forms import CreateProfileFormProfile, CreateProfileFormUser
from profiles.models import Profile


# Create your views here.
@login_required
def profile_list(request):
    users = User.objects.all()
    profiles = Profile.objects.all()

    context = {"users": users, "profiles": profiles}

    return render(request, "profiles/users.html", context)

@login_required
def user_profile(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)

    context = {"profile": profile}

    return render(request, "profiles/user.html", context)

@login_required
def create_profile(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.save()
        upload = request.FILES["upload"]
        file_storage = FileSystemStorage()
        file = file_storage.save(upload.name, upload)
        file_url = file_storage.url(file)
        profile = Profile.objects.create(
            user=request.user,
            about_me=request.POST.get("about_me"),
            photo=file_url
        )
        return redirect("profile", username=request.user.username)

    return render(request, "profiles/create_profile.html", {"form": CreateProfileFormProfile, "form2": CreateProfileFormUser})


def update_profile(request):
    user = get_object_or_404(Profile, username=request.user.username)
    user.first_name = request.POST.get("first_name")
    user.last_name = request.POST.get("last_name")
    user.email = request.POST.get("email")
    user.userprofile.about_me = request.POST.get("about_me")
    user.save()

    return redirect(request.path_info)
