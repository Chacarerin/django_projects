from django.shortcuts import render

def landing(request):
    return render(request, 'landing.html')

def academic(request):
    return render(request, 'academic.html')

def work(request):
    return render(request, 'work.html')