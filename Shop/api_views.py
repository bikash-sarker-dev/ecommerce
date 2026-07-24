from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, permissions, viewsets
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, ProductSerializer
from rest_framework import permissions
from . models import Product


@api_view(['GET'])
def index(request):
    person = {
        'name':'bikash',
        'age':28
    }

    return Response(person)


class Student(APIView):
    def get(self, request):
        student = {
            'student_id' : '012',
            'student_name' : 'shrabon sarker',
            'student_subject' : 'computer sincecs',

        }
        return Response(student)


class ResgisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]



class PrductView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]