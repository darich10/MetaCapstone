from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .serializers import MenuSerializer, BookTableSerializer
from .models import Menu, BookingTable


def say_hello(request):
    return HttpResponse('Hello World')


def index(request):
    return render(request, 'index.html', {})


def get_menu(request):
    menu = MenuSerializer(Menu, many=True)
    return HttpResponse(menu.data)
