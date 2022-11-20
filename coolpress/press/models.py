from django.db import models
#from my_posts.models import *
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Count
from .user_info_manager import get_github_repositories, get_gravatar_image



class CoolUser(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      github_profile = models.CharField(max_length=250, null= True, blank= True)
      git_repo = models.IntegerField(null=True, blank=True)
      grav_link = models.CharField(max_length=420, null=True, blank=True)

      def __str__(self):
          return f'{self.user.first_name} {self.user.last_name} ({self.user.username})'

      def save(self, *args, **kwargs):
          super(CoolUser, self).save(*args, **kwargs)
          email = self.user.email
          if self.gravatar_link is None and email:
              image_link = get_gravatar_image(email)
              if image_link:
                  self.gravatar_link = image_link
                  self.save()
          if self.gh_repositories is None and self.github_profile:
              repositories = get_github_repositories(self.github_profile)
              if repositories is not None:
                  self.gh_repositories = repositories
                  self.save()


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    # def countPosts(self):
    #     category = self
    #     child_catagories = Category.objects.filter(parent = category)
    #     queue = list(child_catagories)
    #     while(len(queue)):
    #         next_children =

    class Meta:
        # enforcing that there can not be two categories under a parent with same slug

        # __str__ method elaborated later in post.  use __unicode__ in place of

        # __str__ if you are using python 2

        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    @property
    def postsCount(self):
        # category = self
        # post_sum = 0
        # child_category = Category.objects.filter(parent = category)
        # queue = list(child_category)
        # while (len(queue)):
        #     next_children = Category.objects.filter(parent = queue[0])
        #     child_category = child_category.union(next_children)
        #     queue.pop(0)
        #     queue = queue + list(next_children)
        #
        # for child in child_category:
        #     post_sum += len(Post.objects.filter(catagory = child))
        #
        # return post_sum
        category = self
        _postsCount = 0
        # get list of children categories
        child_categories = Category.objects.filter(parent=category)
        queue = list(child_categories)
        while len(queue):
            next_children = Category.objects.filter(parent=queue[0])
            child_categories = child_categories.union(next_children)
            queue.pop(0)
            queue += list(next_children)
        # count posts in all related categories
        categories = set(child_categories).union({self})
        for category in categories:
            _postsCount += len(Post.objects.filter(category=category))

        return _postsCount


    # def countPost_EXPERIMENT(self):
    #     categories = Category.objects.all().annotate(post_count=Count("Post"))
    #     for item in categories:
    #         print(categories.post_count)


    def __str__(self):
        full_path = [self.name]
        source = self.parent
        while source is not None:
            full_path.append(source.name)
            source = source.parent
        return ' -> '.join(full_path[::-1])

# Create your models here.






class Post(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(CoolUser,  null=True, blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    content = HTMLField('Content')
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False, )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_cat_list(self):
        k = self.category  # for now ignore this instance method

        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb) - 1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i - 1:-1])
        return breadcrumb[-1:0:-1]

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'comments')
    user = models.ForeignKey(CoolUser, on_delete=models.CASCADE, related_name = 'comments')
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ['created',]
    def __str__ (self):
        return f"Comment by {self.user.user.username} on {self.post}"

