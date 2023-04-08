from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model







# Create your models here.

class Category(models.Model):
    YELLOW = 'bg-yellow-500'
    PINK = 'bg-pink-500'
    ORANGE = 'bg-orange-500'
    BLUE = 'bg-blue-500'
    GREEN = 'bg-green-500'
    RED = 'bg-red-500'
    PURPLE = 'bg-purple-500'
    COLOR_CHOICES = [
        (YELLOW, 'bg-yellow-500'),
        (PINK, 'bg-pink-500'),
        (ORANGE, 'bg-orange-500'),
        (BLUE, 'bg-blue-500'),
        (GREEN, 'bg-green-500'),
        (RED, 'bg-red-500'),
        (PURPLE, 'bg-purple-500'),
    ]


    name = models.CharField(max_length=255)
    color = models.CharField(choices=COLOR_CHOICES, default=ORANGE,  max_length=50)



    class Meta:
        verbose_name_plural = "Categories"

    
    def __str__(self):
        return self.name
    

    def clean(self):
        valid_colors = [choice[0] for choice in self.COLOR_CHOICES]
        if self.color not in valid_colors:
            raise ValidationError({'color': 'Invalid color choice'})
    


class Blogs_Items(models.Model):
    category = models.ForeignKey(Category, related_name='blogs', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='blogs_images', blank=True, null=True)
    is_created = models.BooleanField(default=True, blank=True)
    tags = models.CharField(max_length=255, blank=True)
    likes = models.IntegerField(default=0)
    view_count = models.PositiveIntegerField(default=0)
    published_at = models.DateTimeField(auto_now_add=True)


    def total_likes(self):
        return self.likes.count()



    class Meta:
        verbose_name_plural = "Blogs Posts"


    def __str__(self):
        return self.name
    




class Like(models.Model):
    blog_item = models.ForeignKey(Blogs_Items, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)