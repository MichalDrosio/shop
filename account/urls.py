from django.urls import path
from . import views
from account.views import Register

app_name = 'account'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('user/', views.user_detail, name='user'),
    path('edit/', views.edit_user, name='edit-user'),

]