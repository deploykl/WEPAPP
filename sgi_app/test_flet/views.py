from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'test_flet/index.html')

def testapp(request):
    return render(request, 'test_flet/vista2.py')