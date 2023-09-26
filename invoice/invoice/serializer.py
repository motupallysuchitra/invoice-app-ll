from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username','password','email','name')
    
    def create(self,validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
            email = validated_data['email'],
            name = validated_data['name'],
        )
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
 
    def validate(self,data):
        print("this is data here:")
        print(data)
        user = authenticate(username=data['username'], password=data['password'])
        print(user)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")



# class Userserializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields="__all__"

class Itemserializers(serializers.ModelSerializer):
        class Meta:
                model=Items
                fields="__all__"

class InvoicesSerializer(serializers.ModelSerializer):
    items=Itemserializers(many=True, read_only=True)

    class Meta:
        model=Invoices
        fields="__all__"    