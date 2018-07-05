from django.shortcuts import render

# Create your views here.


def home(request):
    if request.method == 'GET':

        return render(request, 'home.html')


def article(request):
    if request.method == 'GET':
        return render(request, 'article.html')


def detail(request):
    if request.method == 'GET':
        return render(request, 'detail.html')


def about(request):
    if request.method == 'GET':
        return render(request, 'about.html')


def resource(request):
    if request.method == 'GET':
        return render(request, 'resource.html')
