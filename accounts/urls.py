from django.contrib.auth.views import LoginView
from django.urls import path

from .views import SignUpView, UserLoginForm

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(authentication_form=UserLoginForm, template_name="accounts/login.html"), name="login")
]