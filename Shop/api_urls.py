from django.urls import path
from . api_views import index, Student, ResgisterView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [

    path('index/', index),
    path('student/', Student.as_view()),
    path('register/', ResgisterView.as_view(), name='api_register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
   
]

