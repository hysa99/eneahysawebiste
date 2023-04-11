from django.shortcuts import render, get_object_or_404, redirect
from .forms import BlogsForm, CommentsForm
from django.views.decorators.http import require_POST
from .models import Blogs_Items, Category, Like, Comment
from django.http import JsonResponse
from django.urls import reverse

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse







# Create your views here.
def blog_home(request):
    blogs = Blogs_Items.objects.filter(is_created=True)
    categories = Category.objects.all()
    forms = BlogsForm()
    return render(request, 'blogs.html', {
        'blogs': blogs,
        'categories': categories,
        'forms': forms,
    })


def details(request, pk,):
    blogs = Blogs_Items.objects.filter(is_created=True).order_by('-published_at')[0:4]
    categories = Category.objects.all()
    blog = get_object_or_404(Blogs_Items, pk=pk)
    blog.view_count += 1
    blog.save()
    return render(request, 'details.html', {
        'blog': blog,
        'blogs': blogs,
        'categories': categories,
    })


#see how many time the pots have been seeing 
def detail_view(pk):
    blog = get_object_or_404(Blogs_Items, pk=pk)
    blog.view_count += 1
    blog.save()



def like_post(request, pk):
    blog = get_object_or_404(Blogs_Items, pk=pk)
    if request.method == 'POST':
        # Increment the likes field
        blog.likes += 1
        blog.save()
    return HttpResponseRedirect(reverse('blogs:details', args=[pk]))




def load_comment(request):
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            Comment.objects.create(comment=comment)
            return redirect('comment')
        else:
            form = CommentsForm()
            return render(request, 'details.html', {
                'form': form
            })

