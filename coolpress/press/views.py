from django.shortcuts import render
from django.template import loader
from .admin import admin
from django.http import HttpResponse

from .models import Category, Post, CoolUser


def Tests(request):
    data = admin.objec

def authors(request):
    authors_list = CoolUser.objects.all()
    context = {
        "authors_list": authors_list
    }
    return render(request, 'press/index.html', context)

def index(request):
    categories = Category.objects.all()
    latest_post_list = Post.objects.order_by("-publish")[:5]
    context = {
        'categories' : categories,
        'latest_post_list' : latest_post_list
    }
    return render(request, 'press/index.html', context)


