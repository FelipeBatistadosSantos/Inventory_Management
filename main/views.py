from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm, ProductForm
from django.contrib.auth.decorators import permission_required
from .models import Product
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np

def index(request):
    return render(request, 'index.html')

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form':form})    

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('main:pg_management')
    else:
        form = LoginForm() 
    return render(request, 'login.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('main:login')



def estoque_form(request):
    if request.method == 'POST':
        products = ProductForm(request.POST)
        if products.is_valid():
            products.save()
            return redirect('main:pg_management')
    else:
        products = ProductForm()
    return render(request, 'estoque_form.html', {'products': products})

def pg_management(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,"pg_management.html", context)

@permission_required('main.change_product', raise_exception=True)
def alterar_produto(request, produto_id):
    pass

def editar_produto(request, produto_id):
    product = get_object_or_404(Product, id=produto_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('main:pg_management')
    else:
        form = ProductForm(instance=product)
    return render(request, 'editar_produto.html', {'form': form})

def excluir_produto(request, produto_id):
    product = get_object_or_404(Product, id=produto_id)
    if request.method == 'POST':
        product.delete()
        return redirect('main:pg_management')
    return render(request, 'excluir_produto.html', {'product': product})

def categoria_detail(request, categoria_slug):
    categoria_produtos = Product.objects.filter(categoria=categoria_slug)
    return render(request, f'categorias/{categoria_slug}.html', {'categoria_produtos': categoria_produtos})


def editar_produto(request, produto_id):
    # Obter o produto existente pelo ID
    produto = get_object_or_404(Product, id=produto_id)
    
    if request.method == 'POST':
        # Se o formulário for submetido, atualize os dados do produto
        form = ProductForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('main:pg_management')  # Redirecione para a página inicial após a edição
    else:
        # Se o método for GET, preencha o formulário com os dados do produto existente
        form = ProductForm(instance=produto)
        
    return render(request, 'editar_produto.html', {'form': form, 'produto': produto})

def excluir_produto(request):
    if request.method == 'GET':
        produto_id = request.GET.get('id')
        produto = get_object_or_404(Product, id=produto_id)
        produto.delete()
    return redirect('main:pg_management')

from .utils import get_plot
def grafico(request):
    qs = Product.objects.all()
    x = [x.nome for x in qs]
    y = [y.quantidade for y in qs]
    chart = get_plot(x, y)
    return render(request, 'grafico.html', {'chart': chart})

#QUERIES
#############
def filtro():
    resultado = Product.objects.order_by('-quantidade')
    # Converter os resultados para uma lista de listas
    lista_resultados = [[produto.id, produto.nome, produto.quantidade] for produto in resultado]
    # Definir os cabeçalhos da tabela
    cabecalhos = ["ID", "Nome", "Quantidade"]
    # Imprimir a tabela formatada
    print(tabulate(lista_resultados, headers=cabecalhos, tablefmt="grid"))

filtro()

def tudo():
    resultado = Product.objects.all()

    lista = [[produto.id, produto.nome, produto.quantidade, produto.categoria] for produto in resultado]

    cabecalho = ["ID", "Nome", "Quantidade", "Categoria"]

    print(tabulate(lista, headers=cabecalho, tablefmt="grid"))

tudo()    
############