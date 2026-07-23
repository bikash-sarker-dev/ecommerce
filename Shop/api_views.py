from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import permissions


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