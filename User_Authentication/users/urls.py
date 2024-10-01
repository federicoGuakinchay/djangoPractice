from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    # UNLOGINED  PAGES 
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('home/',views.home, name='home'),
    
      #confirm account
    path('confirm/<uidb64>/<token>/', views.confirm_registration, name='confirm_registration'),
    path('succes',views.succes_registration, name='succes'),

    # LOGINED PAGES
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('404/', views.view_404, name='404'),
    path('users/', views.user_list_view, name='user_list'),
    path('user/<int:pk>/', views.user_detail, name='user_detail'),
]