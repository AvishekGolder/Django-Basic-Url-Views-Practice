from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is our home page")

def about(request):
    return HttpResponse("<h1>This is our about page.</h1> ")
def contact(request):
    return HttpResponse("<h1>This is our contact page</h1>")