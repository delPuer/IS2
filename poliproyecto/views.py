from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse


"""
Se definen vistas para la vista home
"""

def home(request):
    """
    Vista de la pagina de inicio, si el usuario ya se encuentra autenticado,
    se muestra el indice
    :param request:
    """
    context = {}
    if request.user.is_authenticated:
        redirect_url = '/index/'
        context['nombre'] = request.user.first_name
    else:
        redirect_url = '/login/'
    return HttpResponseRedirect(redirect_url)

@login_required
def index(request):
    """
    Vista de la pagina de saludo, luego del inicio de sesion
    :param request:
    """
    context = {
        'nombre': request.user.first_name,
        'title': 'Home'
    }
    return render(request, '../templates/accounts/index.html',context)