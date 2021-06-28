from django.shortcuts import render
from .forms import ContatoForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if  form.is_valid():
             form.send_mail()
             messages.success(request, 'Mensagem enviada com sucesso!')
             form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail')
    context = {
        'form' : form
    }
    return render(request, 'contato.html', context)

def produto(request):
    return render(request, 'produto.html')

def about(request):
    return render(request, 'about.html')

def programing(request):
    return render(request, 'programing.html')

def projects(request):
    return render(request, 'projects.html')

def help(request):
    return render(request, 'help.html')
