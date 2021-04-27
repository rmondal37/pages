from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def index(request):
    my_dict = {'insert_me': "Hello there!"}
    render(request, 'pageapp/home.html', context=my_dict)