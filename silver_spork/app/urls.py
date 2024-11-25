from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('courses',views.courses),
    path('contact',views.contact),
    path('about',views.about),
    path('view_courses/<c_id>',views.view_courses),
    ]