from django.shortcuts import render

def home(request):
    return render (request, 'Uesr/index.html')


