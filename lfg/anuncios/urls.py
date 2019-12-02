from django.urls import path

from . import views


app_name = 'anuncios'
urlpatterns = [
    path('anuncios/', views.index, name='index'),

    path('detalhes/<int:anuncio_id>/', views.detail, name='detail'),

    path('create/', views.create, name="create")
]