from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.UserLogin.as_view(), name="Login"),
    path("signup/", views.UserSignup.as_view(), name="Signup")
]