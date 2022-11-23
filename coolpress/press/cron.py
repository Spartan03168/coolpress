from .models import CoolUser
from coolpress.press.scrape import get_all_repositories
from django.contrib.auth.models import User
from datetime import datetime
from libgravatar import Gravatar


def update_model():
    user_ = User.objects.get(username="Spartan03168")
    user = CoolUser.objects.get(user=user_)
    stars = get_all_repositories(user.github_profile)
    if user.github_stars != stars:
        user.github_stars = stars
        user.github_updated_at = datetime.now()
        user.save()


def update_gravitar():
    user_ = User.objects.get(username="Spartan03168")
    user = CoolUser.objects.get(user=user_)
    image = Gravatar(user_.email).get_image()
    print(image)
    if user.gravatar_image_link != image:
        print("changed")
        user.gravatar_image_link = image
        user.gravatar_updated_at = datetime.now()
        user.save()

    print(user.gravatar_updated_at)



