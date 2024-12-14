from django.shortcuts import render

# Create your views here. 

def flowers(request):
    return render(request,'flowers.html') 

def chairs(request):
    return render(request,'chairs.html')
