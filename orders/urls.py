from django.urls import path
from . import views


app_name = 'orders'


urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('history-orders', views.history_orders, name='history_orders'),

]