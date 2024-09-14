from django.urls import path
from blog import views as blog_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('register/', blog_views.RegisterView.as_view(), name='register'),
    path('profile/', blog_views.ProfileView.as_view(), name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
]