from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from chatterbox.forms.forms import RoomEditForm
from chatterbox.models import Room, Message


# Create your views here.
def hello(request, s: str):
    return HttpResponse(f"Hello, {s} world!")

def home(request):
    rooms = Room.objects.all()

    context = {"rooms": rooms}
    return render(request, "chatterbox/home.html", context)

@login_required
def search(request, s: str):
    rooms = Room.objects.filter(name__contains=s)
    messages = Message.objects.filter(body__contains=s)

    return render(request, "chatterbox/search.html", {"rooms": rooms, "messages": messages})

@login_required
def room(request, pk):
    room = Room.objects.get(id=pk)
    messages = Message.objects.filter(room=pk)

    if request.method == "POST":
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get("body")
        )
        return HttpResponseRedirect(request.path_info)

    context = {"room": room, "messages": messages}
    return render(request, "chatterbox/room.html", context)

@login_required
def rooms(request):
    rooms = Room.objects.all()

    context = {"rooms": rooms}

    return render(request, "chatterbox/rooms.html", context)

@login_required
def create_room(request):
    if request.method == "POST":
        room = Room.objects.create(
            host=request.user,
            name=request.POST.get("name"),
            description=request.POST.get("descr")
        )
        return redirect("room", pk=room.id)

    return render(request, "chatterbox/create_room.html")

@login_required
def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    room.delete()

    return redirect("rooms")

@method_decorator(login_required, name="dispatch")
class EditRoom(UpdateView):
    template_name = "chatterbox/edit_room.html"
    model = Room
    form_class = RoomEditForm
    success_url = reverse_lazy("rooms")