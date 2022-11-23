from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'press'
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^posts$', views.posts, name= 'posts'),
    url(r'^authors/', views.authors, name= 'authors'),
    path('base/', views.base, name = 'base'),

]


def commit_trigger():
    pass