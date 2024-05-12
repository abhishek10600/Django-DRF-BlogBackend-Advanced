from django.db import models

# import for registering a user that we use in create_auth_token() method
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


# when the user enters the data and creates an account signal will be passed here and the token for that user will be created and stored in the database. Then that token will be used in the views when we use Token.objects.get(user=account).key

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
