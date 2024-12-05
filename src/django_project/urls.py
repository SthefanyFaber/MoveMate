from django.contrib import admin

from django.urls import path
from MoveMate import views
from django.urls.conf import include
from django.urls.base import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path("login/", LoginView.as_view(template_name="registration/login.html",), name="login"),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy("index"),), name="logout"),
    path('add_post/', views.add_post, name='add_post'),
    path('admin/', admin.site.urls),
    path('register/', views.user_register, name='register'),
    path('post/<int:post_id>/comentar/', views.comentar, name='comentar'),
    path('post/<int:post_id>/curtir/', views.curtir, name='curtir'),
    path('usuario/<int:user_id>/adicionar_amigo/', views.adicionar_amigo, name='adicionar_amigo'),
]