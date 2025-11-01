# live_scores/urls.py
from django.urls import path
from . import views

app_name = "live_scores" 

urlpatterns = [
    path("", views.live_scores, name="scores"),
    path("game/<str:game_id>/", views.game_detail, name="game_detail"),
]
