from django.contrib.auth.models import User
from django.forms import ModelForm
from profiles.models import Profile

class CreateProfileFormProfile(ModelForm):

    class Meta:
        model = Profile
        fields = ["about_me", "photo"]

    def __init__(self, *args, **kwargs):
        super(CreateProfileFormProfile, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class CreateProfileFormUser(ModelForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def __init__(self, *args, **kwargs):
        super(CreateProfileFormUser, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
