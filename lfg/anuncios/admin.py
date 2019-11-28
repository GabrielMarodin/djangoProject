from django.contrib import admin

from .models import Anuncio

class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'publicado', 'data_cadastro', 'user')
    list_display_links = ('id', 'titulo')
    list_filter = ('user',)
    list_editable = ('publicado',)
    search_fields = ('titulo', 'descricao', 'regiao', 'plataforma', 'jogo')
    list_per_page = 15

admin.site.register(Anuncio, AnuncioAdmin)