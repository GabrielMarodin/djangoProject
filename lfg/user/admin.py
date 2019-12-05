from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'data_user')
    list_display_links = ('id', 'username')
    search_fields = ('username', 'email', 'anuncio')
    list_per_page = 25

admin.site.register(User, UserAdmin)
