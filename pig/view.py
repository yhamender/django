from django.http import HttpResponse
from django.shorcuts import render

def hello(request):
	return HttpResponse("helloWorld!")