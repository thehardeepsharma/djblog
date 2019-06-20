from django.urls import path

from . import views

app_name = 'music'

urlpatterns = [
    # ex: /music/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /music/register
    path('register/', views.UserFormView.as_view(), name='register'),
    # /music/album_id/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # /music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name='album_add'),
    # /music/album/1/
    path('album/<int:pk>/', views.AlbumUpdate.as_view(), name='album_update'),
    # /music/album/2/delete/
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album_delete'),
    # /music/album_id/favorite
    # path('<int:pk>/favorite/', views.Favorite.as_view(), name='favorite')
]

