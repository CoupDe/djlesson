from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.

def hello(request):
    return HttpResponse("Main page polls")

def secondpolls(request):
    return HttpResponse("Second page polls")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)