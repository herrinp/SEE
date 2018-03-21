from django.urls import include, path
from . import views

from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('submit_request', views.submit_request, name='submit_request'),
    path('hr_admin_view', views.hr_admin_view, name='hr_admin_view'),
]