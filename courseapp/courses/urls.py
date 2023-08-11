from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('aboutofus', views.aboutofus),
    path('contact',views.contact),
    path('courses', views.courses),
]
