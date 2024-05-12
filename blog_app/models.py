import random
import string

from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.template.defaultfilters import slugify

# Create your models here.


# all the blogs will belong to a category
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    created_at = models.DateField(default=date.today)

    def __str__(self):
        return self.category_name


class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_description = models.TextField()
    # we are adding a author field that uses Uses User model as foreign key. It holds the info of which used created the blog
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="category")  # we will pass the category as foreign key. This field category will be used in the nested serializer
    post_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    slug = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.blog_title  # this is what will be returned when we use StringRelatedField()

    # def save(self, *args, **kwargs):  # this save method is used when we insert the data
    #     if not self.slug:
    #         self.slug = slugify(self.blog_title)
    #     return super().save(*args, **kwargs)

    def save(self, *args, **kwargs):  # this save method is used when we insert the data
        if not self.slug:
            base_slug = slugify(
                self.blog_title + " " + self.author.username + " " + self.category.category_name)  # creating a slug that contains blog title, username and category name
            self.slug = base_slug + \
                "".join(random.choice(string.ascii_letters + string.digits)
                        for _ in range(5))
        return super().save(*args, **kwargs)


class BlogComment(models.Model):
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.blog)
