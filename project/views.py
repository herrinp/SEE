from django.http import HttpResponse
from django.shortcuts import render
from . import templates

# Create your views here.
def index(request):
    return render(request, 'project/templates/index.html', {})