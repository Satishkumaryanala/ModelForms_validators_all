from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse


def insert_topic(request):
    TFO = TopicForm()
    d={'TFO':TFO}
    if request.method == 'POST':
        TFDO = TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('data inserted successfully')
        return HttpResponse('data invalid')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WFO = WebpageForm()
    d={'WFO':WFO}
    if request.method == 'POST':
        WFDO = WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('<center style="color:green;"><h1>Data inserted successfully</h1></center>')

        return HttpResponse('<center style="color:red;"><h1>Data not valid</h1></center>')
    return render(request,'insert_webpage.html',d)