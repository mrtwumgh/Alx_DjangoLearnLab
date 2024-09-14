from django.urls import path
from blog import views as blog_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('register/', blog_views.register, name='register'),
    path('profile/', blog_views.profile, name='profile'),
    path('logout/', blog_views.logout_view, name='logout'),
]