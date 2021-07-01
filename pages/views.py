from django.http import HttpResponse as hr
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
	return hr("<h1>Hello World</h1>")

def contact_view(*args, **kwargs):
	return hr("<h1>Contact View</h1>")