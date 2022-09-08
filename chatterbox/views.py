from django.http import HttpResponse
from django.shortcuts import render

from chatterbox.models import Room, Message


# Create your views here.
def hello(request, s: str):
    return HttpResponse(f"Hello, {s} world!")


def search(request, s: str):
    rooms = Room.objects.filter(name__contains=s)
    messages = Message.objects.filter(body__contains=s)

    return render(request, "chatterbox/search.html", {"rooms": rooms, "messages": messages})
