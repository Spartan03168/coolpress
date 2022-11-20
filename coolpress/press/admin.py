from django.contrib import admin

from .models import Category, Post, CoolUser, Comment

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(CoolUser)
admin.site.register(Comment)



# Register your models here.

