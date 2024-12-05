from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['conteudo', 'imagem_url']
        widgets = {
            'conteudo': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
