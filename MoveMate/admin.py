from django.contrib import admin
from .models import Categoria, Item

class ItemInline(admin.TabularInline):
    model = Item
    extra = 1  

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'icone', 'descricao')
    inlines = [ItemInline]

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Item)