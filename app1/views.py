from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def abhi(request):
    return HttpResponse('<h1>Hello .....</h1>')
def abhi(request):
    return render(request,'abhi.html')