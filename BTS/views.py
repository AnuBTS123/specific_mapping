from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def jungkook(request):
    return render(request,'jungkook.html')

def jhope(request):
    return  HttpResponse('<h1>jhope is an sunshine of BTS</h1>')