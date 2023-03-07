from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app2_first(request):
    return HttpResponse("<h1>this my app2 first application</h1>")

def app2_second(request):
    return HttpResponse("<h1>this my app2 second application</h1>")