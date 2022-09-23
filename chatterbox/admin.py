from django.contrib import admin

from chatterbox.models import Room, Message
from profiles.models import Profile

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Profile)