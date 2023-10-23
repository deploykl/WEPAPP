from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.LOGIN, name='index'),
    path('admin/', admin.site.urls),
    path('flet/', include('test_flet.urls')),
    path('accounts/', include('django.contrib.auth.urls'), name='login'),
    path('logout/', views.LOGOUT, name='logout'),

]
