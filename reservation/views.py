from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def say_hello(request):
    return HttpResponse('Hello World')


def index(request):
    return render(request, 'index.html', {})