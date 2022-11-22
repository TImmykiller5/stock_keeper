from django.urls import path
from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.Things.as_view(), name='things'),
    path('store_add', views.StoreAdd.as_view(), name='StoreAdd'),
    path('store', views.StockView.as_view(), name='StockList'),
]