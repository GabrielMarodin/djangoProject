from django.urls import path

from . import views


app_name = 'anuncios'
urlpatterns = [
    path('', views.index, name='index'),

    path('detalhes/<int:anuncio_id>/', views.detail, name='detail'),

]