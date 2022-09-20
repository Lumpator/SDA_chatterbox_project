from django import forms
from django.forms import ModelForm

from chatterbox.models import Room


class RoomEditForm(ModelForm):

    class Meta:
        model = Room
        fields = "__all__"
