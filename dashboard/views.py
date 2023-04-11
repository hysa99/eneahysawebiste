from django.shortcuts import render
from blogs.models import Blogs_Items, Category
from django.db.models import Count






# Create your views here.

def dashboard_view(request):
    blog_count = Blogs_Items.objects.all().count()
    categories = Category.objects.annotate(post_count=Count('blogs')).all()

    for category in categories:
        print(category.post_count)


    return render(request, 'dashboard.html', {
        'blog_count': blog_count,
        'categories': categories,
    })

