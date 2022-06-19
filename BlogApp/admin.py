from django.contrib import admin
from BlogApp.models import Comentarios
from BlogApp.models import Post
# Register your models here.
admin.site.register(Post)
admin.site.register(Comentarios)