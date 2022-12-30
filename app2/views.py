from django.shortcuts import render

# Create your views here.
def html(request):
    return render(request,'html.html')

def appp2fil(request):
    return render(request,'appp2fil.html')

def a2f2(request):
    return render(request, 'a2f2.html')