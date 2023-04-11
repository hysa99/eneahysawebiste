from django.shortcuts import render, redirect
from blogs.models import Blogs_Items



# Create your views here.
def home(request):
    blogs = Blogs_Items.objects.filter(is_created=True).order_by('-published_at')[0:4]

    return render(request, 'index.html', {
        'blogs': blogs,
    })