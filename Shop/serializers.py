from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Product, Card, Customer







class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, required=True)
    password2 = serializers.CharField(write_only = True, required=True)

    class Meta:
        model = User
        fields = ('username','email','password', 'password2')


    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'passowrd':'password field do not match.'})
        return data


    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        return user



class ProductSerializer(serializers.ModelSerializer):
    product_image = serializers.ImageField(read_only=True)

    class Meta:
        model= Product
        fields = ['id', 'title','selling_price','discounted_price','description','brand','category','product_image']


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        write_only=True, 
        source='product', 
        queryset=Product.objects.all()
        )
    user = serializers.PrimaryKeyRelatedField(
        read_only=True, 
        default=serializers.CurrentUserDefault() 
        )
    total_cust = serializers.SerializerMethodField()

    class Meta:
        model =  Card
        fields = ['id', 'user', 'product', 'product_id', 'quantity', 'total_cust']
    def get_total_cust(self, obj):
        return obj.total_cust


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']




class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = ['id','user', 'name','division','district','thana','villorroad','zipCode']