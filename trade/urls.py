from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('cadastro_clientes/', views.cadastro_clientes, name='cadastro_clientes'),
    path('cadastro_usuario/', views.cadastro_usuario, name='cadastro_usuario'),
    path('demonstrativo_tabelas/', views.demonstrativo_tabelas, name='demonstrativo_tabelas'),
    path('galeria_produtos/', views.galeria_produtos, name='galeria_produtos'),
    path('realizar_venda/', views.realizar_venda, name='realizar_venda'),
]
