from django.shortcuts import render

def home(request):
    return render (request, 'User/index.html')


def register(request):
    return render(request, 'User/register.html')

