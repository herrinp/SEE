from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('kiosk/', include('kiosk.urls')),
    path('SEE/', include('SEE.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
