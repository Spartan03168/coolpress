from django.contrib import admin

from .models import Category, Post, Extra

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Extra)
#admin.site.register(cool_user)

# Register your models here.

def update_trigger():
    pass