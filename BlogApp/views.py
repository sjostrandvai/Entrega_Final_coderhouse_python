from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from BlogApp.forms import ComentarioForm
from BlogApp.models import Comentarios
from BlogApp.forms import PostForm

from BlogApp.models import Post

# Create your views here.


def home(request):
    return render(request, 'BlogApp/home.html')


def about(request):
    return render(request, 'BlogApp/about.html')


def pages(request):

    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'BlogApp/pages.html', context)


def createPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            autor = request.user
            post = Post(titulo=data['titulo'], subtitulo=data['subtitulo'],
                        contenido=data['contenido'], autor=autor, imagen=data['imagen'])
            post.save()
            post = Post.objects.all()
            context = {'posts': post}
            return render(request, 'BlogApp/pages.html', context)
    else:
        form = PostForm()

    return render(request, 'BlogApp/createPost.html', {'form': form})

def getPost(request, id):
    post = Post.objects.get(id=id)
    comentarios = Comentarios.objects.filter(post=post)
    return render (request, 'BlogApp/post.html', {'post': post, 'comentarios': comentarios})

def deletePost(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    post = Post.objects.all()
    context = {'posts': post}
    return render(request, 'BlogApp/pages.html', context)

def editPost(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post.titulo = data['titulo']
            post.subtitulo = data['subtitulo']
            post.contenido = data['contenido']
            post.imagen = data['imagen']
            post.save()
            post = Post.objects.all()
            context = {'posts': post}
            return render(request, 'BlogApp/pages.html', context)
    else:
        form = PostForm(initial={ 'titulo': post.titulo, 'subtitulo': post.subtitulo, 'contenido': post.contenido, 'imagen': post.imagen})
    return render(request, 'BlogApp/editPost.html', {'form': form})

def addComment(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            comentario = Comentarios(comentario=data['comentario'], autor=request.user, post=post)
            comentario.save()
            post = Post.objects.all()
            context = {'posts': post}
            return render(request, 'BlogApp/pages.html', context)
    else:
        form = ComentarioForm()
    return render(request, 'BlogApp/addComment.html', {'form': form, 'post':post})