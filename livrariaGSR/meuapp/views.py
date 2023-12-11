from django.shortcuts import render
from .models import Livro

def home(request):
    return render(request, 'index.html')

def cadastrar_livro(request):
    if request.method == 'POST':
        # Lógica para cadastrar um livro usando informações do formulário
        return render(request, 'mensagem.html', {'mensagem': 'Livro cadastrado com sucesso!'})
    return render(request, 'cadastrar_livro.html')

def pesquisar_livro(request):
    if request.method == 'GET':
        termo_busca = request.GET.get('termo_busca')
        livros_encontrados = Livro.objects.filter(titulo__icontains=termo_busca)
        return render(request, 'resultado.html', {'livros_encontrados': livros_encontrados, 'termo_busca': termo_busca})
    return render(request, 'pesquisar.html')
