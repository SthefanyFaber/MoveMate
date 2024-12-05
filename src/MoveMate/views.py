from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .models import Post, Amigo, Comentario, Curtida
from .forms import PostForm

@login_required
def adicionar_amigo(request, user_id):
    amigo = get_object_or_404(User, id=user_id)
    if not Amigo.objects.filter(usuario=request.user, amigo=amigo).exists():
        Amigo.objects.create(usuario=request.user, amigo=amigo)
        messages.success(request, f"{amigo.username} foi adicionado como amigo!")
    else:
        messages.info(request, f"{amigo.username} já é seu amigo.")
    return redirect('index')

@login_required
def index(request):
    if request.user.is_authenticated:
        amigos = Amigo.objects.filter(usuario=request.user)
        amigo_ids = [amigo.amigo.id for amigo in amigos]
        posts = Post.objects.filter(usuario__in=amigo_ids) | Post.objects.all()
    else:
        posts = Post.objects.all()

    return render(request, 'index.html', {'posts': posts})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = request.user
            post.save()
            messages.success(request, 'Post criado com sucesso!')
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso! Agora, faça login.')
            return redirect('login')
        else:
            messages.error(request, 'Erro ao criar a conta. Tente novamente.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def comentar(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        texto = request.POST.get('texto')
        if texto:
            Comentario.objects.create(post=post, usuario=request.user, texto=texto)
    return redirect('index')

@login_required
def curtir(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    curtida, created = Curtida.objects.get_or_create(post=post, usuario=request.user)
    if not created:
        curtida.delete()
    return redirect('index')
