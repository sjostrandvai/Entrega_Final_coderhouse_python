from django import forms


class PostForm(forms.Form):
    titulo = forms.CharField(max_length=200)
    subtitulo = forms.CharField(max_length=200)
    contenido = forms.CharField(max_length=500)
    imagen = forms.ImageField(required=False)


class ComentarioForm(forms.Form):
    comentario = forms.CharField(max_length=500)
