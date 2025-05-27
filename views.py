from django.shortcuts import render

# Create your views here.
def pedros(request):
    return render(request, 'pedros/home.html')

def about(request):
    return render(request, 'pedros/about.html'),

def projects(request):
    return render(request, 'pedros/projects.html'),

