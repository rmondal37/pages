from django.shortcuts import render

from django.http import HttpResponse
from .models import Topic, WebPage, AccessRecord

# Create your views here.


def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    return render(request, 'pageapp/home.html', context=date_dict)