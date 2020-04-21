from django.urls import path
from . import views
from .views import Register

app_name = 'account'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', Register.as_view(), name='register'),

]