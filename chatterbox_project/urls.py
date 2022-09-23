"""chatterbox_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import chatterbox.views
import profiles.views

urlpatterns = [
    #chatterbox app
    path('', chatterbox.views.home, name='home'),
    path('admin/', admin.site.urls),
    path('hello/<s>', chatterbox.views.hello),
    path('search/', chatterbox.views.search, name="search"),
    path('room/<str:pk>/', chatterbox.views.room, name="room"),
    path("rooms/", chatterbox.views.rooms, name="rooms"),

    #accounts app
    # accounts aplikace
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('create_room/', chatterbox.views.create_room, name="create_room"),
    path("delete_room/<str:pk>", chatterbox.views.delete_room, name="delete_room"),
    path("edit_room/<str:pk>", chatterbox.views.EditRoom.as_view(), name="edit_room"),

    path("__reload__/", include("django_browser_reload.urls")),

    # profiles aplikace
    path("users/", profiles.views.profile_list, name="profiles"),
    path("user/<str:pk>", profiles.views.user_profile, name="profile"),

]
