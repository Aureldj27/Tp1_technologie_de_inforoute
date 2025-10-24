from core.models import Dataset
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.



def home(request):
	return HttpResponse("<html><body><p> je suis fans catalog</p></body></html>")