from django import forms
from django.forms import ModelForm

from chatterbox.models import Room


class RoomEditForm(ModelForm):

    class Meta:
        model = Room
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(RoomEditForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class RoomCreateForm(ModelForm):

    class Meta:
        model = Room
        fields = ["name", "description"]

    def __init__(self, *args, **kwargs):
        super(RoomCreateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
