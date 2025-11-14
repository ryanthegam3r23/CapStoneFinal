# users/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'users'

urlpatterns = [
    path("login/", views.UserLogin.as_view(), name="login"),
    path("signup/", views.UserSignup.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(template_name='users/logged_out.html'), name="logout"),
]
