from django.urls import path
from . import views


app_name = 'orders'


urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('history-order/', views.orders_history, name='history'),
    path('detail-order/<int:id>', views.detail_order, name='detail_order')




]