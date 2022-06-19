from django.db import models

# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='images/', blank=True, null=True)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return f"Titulo: {self.titulo} - Autor: {self.autor} Fecha: {self.fecha_creacion}"

class Comentarios(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comentario = models.TextField()
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
