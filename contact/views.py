from django.core.mail import EmailMessage
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from contact.forms import ContatoForm
from django.contrib import messages
from django.shortcuts import render
from django.template.loader import render_to_string
from django.core import mail
from django.conf import settings
# Create your views here.

def contact(request):
    if (request.method == 'POST'):
        return create(request)
    else:
        return new(request)


def create(request):
    form = ContatoForm(request.POST)

    if not form.is_valid():
        return render(request, 'contact/contact_form.html', {'form': form})


    _send_mail(
        'contact/contact_email.txt',
        form.cleaned_data,
        'Confirmação de contato.',
        form.cleaned_data['email'],
        settings.DEFAULT_FROM_EMAIL)
    messages.success(request, 'Contato realizado')
    return HttpResponseRedirect('/contato/')

def new(request):
    return render(request, 'contact/contact_form.html', {'form': ContatoForm()})

def _send_mail(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    email = mail.send_mail(subject, body, from_, [from_, to])





# def enviar_email(request):
#     if request.method == 'POST':
#         form = ContatoForm(request.POST)
#         if form.is_valid():
    
#             nome = form.cleaned_data['name']
#             email = form.cleaned_data['email']  
#             mensagem = form.cleaned_data['message']

#             assunto = f"Mensagem de {nome}"
#             mensagem_completa = f"Nome: {nome}\nE-mail: {email}\n\nMensagem:\n{mensagem}"

#             _send_mail(
#             subject=assunto,                
#             body=mensagem_completa,         
#             from_email=email,               
#             to=['contato@eventif.com.br'],    
#             cc=[email], 
#             )
#             messages.success(request, 'E-mail enviado com sucesso!')
#             return HttpResponseRedirect('/contato/')
#     else:
#         form = ContatoForm()
#     return render(request, 'contact/contact_form.html', {'form': ContatoForm()})

