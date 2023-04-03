from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager




# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)


    class Meta:
        verbose_name_plural = "Categories"

    
    def __str__(self):
        return self.name
    


class Blogs_Items(models.Model):
    category = models.ForeignKey(Category, related_name='blogs', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='blogs_images', blank=True, null=True)
    is_created = models.BooleanField(default=True, blank=True)
    tags = TaggableManager()
    published_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Blogs Posts"


    def __str__(self):
        return self.name
