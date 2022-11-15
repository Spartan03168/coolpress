from django.shortcuts import render
from django.template import loader
from .admin import admin
from django.http import HttpResponse

def Tests(request):
    data = admin.objec


def index(request):
    return HttpResponse("Welcome to the press.")


