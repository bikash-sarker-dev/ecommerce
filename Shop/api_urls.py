from django.urls import path
from . api_views import index, Student, ResgisterView

urlpatterns = [

    path('index/', index),
    path('student/', Student.as_view()),
    path('register/', ResgisterView.as_view(), name='api_register'),
   
]

