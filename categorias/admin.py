from django.contrib import admin
from .models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(Categoria, CategoriaAdmin)
