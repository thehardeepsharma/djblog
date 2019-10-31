from django.urls import path

from . import views

app_name = 'my_dashboard'

urlpatterns = [
    # /my_dashboard/
    path('', views.DashboardView.as_view(), name='index')
]

