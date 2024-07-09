from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the home page.")


def test(request):
    return HttpResponse('<h1>Hello, world.</h1>')
