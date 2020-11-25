from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('album/new/', views.album_new, name='album_new'),
    path('artist/new/', views.artist_new, name='artist_new'),
]
