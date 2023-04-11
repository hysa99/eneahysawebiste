from django.shortcuts import render
from .models import Projects
from blogs.models import Blogs_Items




# Create your views here.
def Addition(num1, num2):
    result = int(num1) + int(num2)
    return result



def Substraction(num1, num2):
    result = int(num1) - int(num2)
    return result



def Divide(num1, num2):
    result = int(num1) / int(num2)
    return result



def Multiply(num1, num2):
    result = int(num1) * int(num2)
    return result



def projects_home(request):
    projects = Projects.objects.filter(input=True)
    result = None
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']

        if 'add' in request.POST:
            result = Addition(num1, num2)
            return render(request, 'projects.html', {
                'result': result
            })

        if 'sub' in request.POST:
            result = Substraction(num1, num2)
            return render(request, 'projects.html', {
                'result': result
            })

        if 'div' in request.POST:
            result = Divide(num1, num2)
            return render(request, 'projects.html', {
                'result': result
            })

        if 'mult' in request.POST:
            result = Multiply(num1, num2)
            return render(request, 'projects.html', {
                'result': result
            })

    return render(request, 'projects.html', {
        'projects': projects,
        })

