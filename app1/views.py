from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_first(request):
    return HttpResponse("<h1><marquee>this is my app1 first application</h1></marquee>")


def app1_second(request):
    return HttpResponse("<h1>this  my app1 second apllication<h1>")