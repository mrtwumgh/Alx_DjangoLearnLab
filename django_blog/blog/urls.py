from django.urls import path
from blog import views as blog_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('register/', blog_views.register, name='register'),
    path('profile/', blog_views.profile, name='profile'),
    path('logout/', blog_views.logout_view, name='logout'),
    path('', blog_views.HomePostListView.as_view(), name='home'),
    path('posts/', blog_views.PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', blog_views.PostDetailView.as_view(), name='post-detail'),
    path('posts/new/', blog_views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', blog_views.PostUpdateView.as_view(), name='post-edit'),
    path('posts/<int:pk>/delete/', blog_views.PostDeleteView.as_view(), name='post-delete'),
]