from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    # ex: /blog/
    path('', views.PostListView.as_view(), name='index'),
    # ex: /post/5/
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    # ex: /post/new/
    path('post/new/', views.PostView.as_view(), name='post_new'),
    # ex: /post/5/edit/
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

