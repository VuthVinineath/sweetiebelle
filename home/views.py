from django.shortcuts import render

# Create your views here.

def home(request):
    data = {'data':1}
    return render(request,'home/home.html',data)
