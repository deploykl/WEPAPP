from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.INDEX, name='index'),
    path('admin/', admin.site.urls),
    path('flet/', include('test_flet.urls')),

]
