from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
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
        if request.FILES.get("upload"):
            upload = request.FILES["upload"]
            file_storage = FileSystemStorage()
            file = file_storage.save(upload.name, upload)
            file_url = file_storage.url(file)
        else:
            file_url = "/media/no_image.png"
        profile = Profile.objects.create(
            user=request.user,
            about_me=request.POST.get("about_me"),
            photo=file_url
        )
        return redirect("profile", username=request.user.username)

    return render(request, "profiles/create_profile.html", {"form": CreateProfileFormProfile, "form2": CreateProfileFormUser})

@login_required
def update_profile(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.email = request.POST.get("email")
            user.save()
            profile = Profile.objects.get(user=user)
            profile.about_me = request.POST.get("about_me")
            profile.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def update_photo(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        if request.FILES:
            photo = request.FILES["upload_new_photo"]
            file_storage = FileSystemStorage()
            file = file_storage.save(photo.name, photo)
            file_url = file_storage.url(file)
            profile = Profile.objects.get(user=user)
            profile.photo = file_url
            profile.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))