from django.contrib import admin
from django.urls import path
from . import views

app_name = 'alphavantage_app'

urlpatterns = [
    path('data/', views.data_view, name='av_data'),
    path('data/export/<slug:api_detail>/<slug:parent_symbol>/<slug:symbol>/<slug:data_type>/', 
    	views.export_data, name='export_av_data'),
]
