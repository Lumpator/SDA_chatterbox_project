from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created", "-updated"]

    def __str__(self):
        return self.name

    def message_count(self):
        room_messages = Message.objects.filter(room=self.id)
        return room_messages.count()


class Message(models.Model):
    body = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="usermsg")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created", "-updated"]

    def __str__(self):
        return self.body

