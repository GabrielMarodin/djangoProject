from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'data_user')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'email', 'anuncio')
    list_per_page = 25

admin.site.register(User, UserAdmin)
