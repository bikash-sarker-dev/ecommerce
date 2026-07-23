from rest_framework import serializers
from django.contrib.auth.models import User






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


