from django.shortcuts import render, get_object_or_404
from .forms import BlogsForm

from .models import Blogs_Items




# Create your views here.
def blog_home(request):
    blogs = Blogs_Items.objects.filter(is_created=True)

    return render(request, 'blogs.html', {
        'blogs': blogs,
    })


def details(request, pk):
    blog = get_object_or_404(Blogs_Items, pk=pk)

    return render(request, 'details.html', {
        'blog': blog
    })