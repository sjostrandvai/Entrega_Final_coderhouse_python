from django.urls import path
from AccountsApp import views
from django.contrib.auth.views import LogoutView
from BlogApp import views as blog_views

urlpatterns = [
    path('', views.login_request, name='login'),
    path('logout', LogoutView.as_view(template_name='AccountsApp/logout.html'), name='logout'),
    path('edit', views.edit, name='edit'),
    path('signup', views.signup, name='signup'),
    path('home', blog_views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('upload', views.uploadAvatar, name='upload'),
]
