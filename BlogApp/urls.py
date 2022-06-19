from django.urls import path
from BlogApp import views
from AccountsApp import views as accounts_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pages/', views.pages, name='pages'),
    path('login/', accounts_views.login, name='login'),
    path('profile', accounts_views.profile, name='profile'),
    path('createPost', views.createPost, name='createPost'),
    path('pages/<id>', views.getPost, name='getPost'),
    path('pages/<id>/delete', views.deletePost, name='deletePost'),
    path('pages/<id>/edit', views.editPost, name='editPost'),
    path('pages/<id>/addComment/', views.addComment, name='addComment'),
]
