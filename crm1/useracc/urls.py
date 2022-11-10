from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('user/', views.user, name='user'),
    path('logout/', views.logoutuser, name='logout'),
    path('reserve/', views.create_order, name='reserve')
]
