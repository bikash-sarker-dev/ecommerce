from django.urls import path
from . api_views import index, Student

urlpatterns = [

    path('index/', index),
    path('student/', Student.as_view()),
   
]

