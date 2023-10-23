from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def LOGIN(request):
    return render(request, 'index.html', None)

# SALIDA DE LA SESION
def LOGOUT(request):
    logout(request)
    return redirect('index')