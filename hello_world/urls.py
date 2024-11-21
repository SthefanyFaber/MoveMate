from django.contrib import admin
from django.urls import path
from MoveMate import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('login/', views.user_login, name='login'),  # Página de login
    path('logout/', views.user_logout, name='logout'),  # Página de logout
    path('add_post/', views.add_post, name='add_post'),  # Página para adicionar post
    path('admin/', admin.site.urls),  # Admin do Django
    path('register/', views.user_register, name='register')  # Página de registro
]
