from django.urls import path, include
from . api_views import (index, Student, ResgisterView, PrductView)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', PrductView, basename='products')

urlpatterns = [
    path('', include(router.urls)),
    path('index/', index),
    path('student/', Student.as_view()),
    path('register/', ResgisterView.as_view(), name='api_register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
   
]

