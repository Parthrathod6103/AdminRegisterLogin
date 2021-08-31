from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls import url

# So we can use it like: {% url 'myapp:user_register' %} on our template.
urlpatterns = [
    path('', views.home, name='main-home'),
     path('About/', views.About, name='about'),
     path('Contact/', views.Contact, name='contact')
]