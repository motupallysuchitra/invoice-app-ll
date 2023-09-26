from django.shortcuts import render
from django.views import View
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .data import *
from .models import *
from django.http import JsonResponse
import uuid
import json

# Create your views here.

class AllInvoices(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request): 
        invoices = Invoices.objects.filter(user=request.user.id)
        serializer = InvoicesSerializer(invoices,many=True).data
        return Response(serializer,status=status.HTTP_200_OK)


    def post(self,request):
        data = request.data
        data["user"] = request.user.id
    
   
      
        serializer = InvoicesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
         
  


class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Äccount created successfully"}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SigninView(APIView):
    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            user = serializer.validated_data
            # print(user)
            token = RefreshToken.for_user(user)
            # return Response({"messages":"login done"},status = status.HTTP_200_OK)
            return Response({"message": "login done", "access_token": str(token.access_token), "refresh_token": str(token)}, status=status.HTTP_200_OK)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
                
      
    
class SpecificInvoices(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            print(request.user)
            invoice = Invoices.objects.get(invoice_id=id, user= request.user.id)
            serializer = InvoicesSerializer(invoice).data
            return Response(serializer, status=status.HTTP_200_OK)
        except Invoices.DoesNotExist:
            return Response({"message": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)

class AddItem(APIView):
    def post(self, request, id):
        data = request.data
        data["invoices"] = id
        serializer = Itemserializers(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
                        





