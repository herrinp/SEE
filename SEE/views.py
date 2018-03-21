from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def submit_request(request):
    return render(request, 'SEE/templates/submit_request.html', {})

def hr_admin_view(request):
    return render(request, 'SEE/templates/hr_admin_view.html', {})

def index(request):
    return HttpResponse("SEE index page")