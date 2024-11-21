from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    icone = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    tempo_recomendado = models.IntegerField(default=30)
    valor_calorico = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    tipo_categoria = models.CharField(
            max_length=20,
            choices=[('nutrição', 'Nutrição'), ('exercicio', 'Exercício')],
            default='exercicio'
        )
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.nome


class Item(models.Model):
    nome = models.CharField(max_length=255)
    link = models.URLField(max_length=200, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    duracao = models.IntegerField(default=30)
    calorias = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    tipo_item = models.CharField(
            max_length=20,
            choices=[('exercicio', 'Exercício'), ('receita', 'Receita')],
            default='exercicio'
        )
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

def __str__(self):
    return f"{self.nome} - {self.categoria.nome} ({self.usuario.username})"


class Post(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    imagem_url = models.URLField(max_length=200, blank=True, null=True)  
    data_postagem = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f'{self.usuario.username} - {self.data_postagem}'


class Amigo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario')
    amigo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='amigo')

def __str__(self):
        return f'{self.usuario.username} e {self.amigo.username}'