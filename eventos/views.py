from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import  HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from eventos.models import *
from datetime import datetime

# Create your views here.
def getAll(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/index.html', {'eventos': eventos})
    #return HttpResponse("Text only, please.", content_type="text/plain")

@login_required()
@csrf_exempt
def postEvento(request):
    if request.method=='POST':
        es = Espacio.objects.get(pk=request.POST['espacio'])
        now = datetime.today().strftime('%Y-%m-%d')
        e = Evento.objects.create(descripcion = request.POST['descripcion'], fecha = now, espacio = es)
        e.save()
        return redirect('/eventos')
    else:
        espacios = Espacio.objects.all()
        return render(request, 'eventos/registracion.html', {'espacios': espacios})


@csrf_exempt
def user_login(request):
    error=''
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        #pdb.set_trace()
        if user is not None:
           if user.is_active:
               login(request, user) # ????
               if request.GET.get('next') is None:
                   return redirect('login')
               else:
                   return redirect(request.GET.get('next'))

           else:
               error='usuario inactivo'
               return render(requeset, 'eventos/login.html', {'error': error})
               # Return a 'disabled account' error message
        else:
           error='Usuario y/o clave incorrecta'
           return render(request, 'eventos/login.html', {'error': error})
           # Return an 'invalid login' error message.
    else:
        return render(request, 'eventos/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
