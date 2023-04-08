from django.shortcuts import render
from .models import Projects




# Create your views here.
def projects_home(request):
    projects = Projects.objects.filter(input=True)

    return render(request, 'projects.html', {
        'projects': projects,
        })