from django.urls import path
from . import views
urlpatterns = [
    path("list/", views.StatList.as_view(), name="stat_list"),
    path("detail/<int:pk>/", views.StatDetail.as_view(), name="stat_detail" ), 
]