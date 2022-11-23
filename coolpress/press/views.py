from django.db.models import Model
from django.shortcuts import render
from django.http import JsonResponse
from django.template import loader
from .admin import admin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import PostForm, CommentForm
from .models import Category, Post, CoolUser

@csrf_exempt
def createPost(request):
    if request.method == 'POST':
        postform = PostForm(request.POST)
        if postform.is_valid():
            postform.save()
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@csrf_exempt
def postComment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@csrf_exempt
def getPost_by_user(request):
    if request.method == 'GET':
        user_ = User.object.get(username = request.GET.get('username'))
        user = CoolUser.object.get(user = user_)
        allPosts = Post.objects.filter(author=user)
        print(allPosts)
        return JsonResponse({'Success': True})
    return JsonResponse({'Success': False})

@csrf_exempt
def getPost_by_category(request):
    if request.method == 'GET':
        category = Category.objects.get(name = request.GET.get('category'))
        allPosts = Post.objects.filter(category = category)
        print(allPosts)
        return JsonResponse({'Success': True})
    return JsonResponse({'Success': False})

@csrf_exempt
def getUser_by_categorySlug(request):
    if request.method == 'GET':
        allPosts = Post.objects.filter(slug = request.GET.get('slug'))
        allAuthors = []
        for posts in allPosts:
            allAuthors.append(posts.author)
        print(allAuthors)
        return JsonResponse({'Success': True})
    return JsonResponse({'Success': False})





def Tests(request):
    data = admin.object

def authors(request):
    authors_list = CoolUser.objects.all()
    context = {
        "authors_list": authors_list
    }
    return render(request, 'press/authors.html', context)

def index(request):
    categories = Category.objects.all()
    latest_post_list = Post.objects.order_by("-publish")[:5]
    context = {
        'categories' : categories,
        'latest_post_list' : latest_post_list
    }
    return render(request, 'press/index.html', context)

def base(request):
    return render(request, 'press/base.html',{})




