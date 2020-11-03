from django.urls import path

from . import views

urlpatterns = [
    path('<str:album>/', views.album, name="album"),
]