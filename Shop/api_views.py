from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import generics, permissions, viewsets
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, ProductSerializer, CartSerializer , CustomerSerializer, OrderPlaceSerializer
from rest_framework import permissions, status
from . models import Product, Card, OrderPlaced


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


class CartViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartSerializer

    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)

    # def get_serializer_class(self):
    #     if self.action in ['create','update', 'partial_update']:
    #         return Car


    @action(detail=True, methods=['post'])
    def increment(self, request, pk=None):
        cart_item = self.get_object()
        cart_item.quantity += 1
        cart_item.save()
        return Response(CartSerializer(cart_item, context={'request': request}).data)

    @action(detail=True, methods=['post'])
    def decrement(self, request, pk=None):
        cart_item = self.get_object()

        if cart_item.quantity > 1:

            cart_item.quantity -= 1
            cart_item.save()
            return Response(CartSerializer(cart_item, context={'request':request}).data)
        else:
            cart_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['delete'])
    def cartdelete(self, request, pk=None):
        cart_item = self.get_object()
        cart_item.delete()
        return Response({'message':'cart delete successfull'}, status=status.HTTP_200_OK)




class CustomerCreateView(generics.CreateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class OrderViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAuthenticated]
    serializer_class = OrderPlaceSerializer

    def get_queryset(self):
        return OrderPlaced.objects.filter(user=self.request.user).order_by('-ordered_date')