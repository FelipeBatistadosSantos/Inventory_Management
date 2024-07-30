from django.urls import path
from .views import index, user_login, user_signup, grafico, categoria_detail, user_logout, estoque_form, pg_management, excluir_produto, editar_produto


app_name = 'main'

urlpatterns = [
    path('', index, name='home'),
    path('login', user_login, name='login'),
    path('signup', user_signup, name='signup'),
    path('logout', user_logout, name='logout'),
    path('estoque_form', estoque_form, name='estoque_form'),
    path('pg_management', pg_management, name='pg_management'),
    path('editar_produto/<int:produto_id>/', editar_produto, name='editar_produto'),
    path('excluir_produto/<int:produto_id>/', excluir_produto, name='excluir_produto'),
    path('categoria/<slug:categoria_slug>/', categoria_detail, name='categoria_detail'),
    path('editar_produto/', editar_produto, name='editar_produto'),
    path('excluir_produto/', excluir_produto, name='excluir_produto'),
    path('grafico/', grafico, name='grafico'),
]