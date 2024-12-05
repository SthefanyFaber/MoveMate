from django.contrib import admin
from .models import Categoria, Item, Post, Amigo, Comentario, Curtida

class ItemInline(admin.TabularInline):
    model = Item
    extra = 1

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'icone', 'descricao')
    inlines = [ItemInline]

class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 1

class CurtidaInline(admin.TabularInline):
    model = Curtida
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'conteudo', 'data_postagem')
    inlines = [ComentarioInline, CurtidaInline]

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Item)
admin.site.register(Post, PostAdmin)
admin.site.register(Amigo)
admin.site.register(Comentario)
admin.site.register(Curtida)
