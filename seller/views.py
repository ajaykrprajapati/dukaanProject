from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
import json
from rest_framework.response import Response
from .models import Account, Store
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .serializers import OwnerSerializer, StoreSerializer
from buyer.serializers import ProductSerializer
from rest_framework.generics import CreateAPIView


class OwnerSignUpAPIView(APIView):
    def post(self, request):
        data = request.data
        user = request.user
        serializer = OwnerSerializer(data=data)      
        if serializer.is_valid():
            print("valie")
            serializer.save()
        else:
            print(serializer.errors)
        owner = Account.objects.get(username=serializer.data['phone_number'])
        token, created=Token.objects.get_or_create(user=owner)
        user_serializer = OwnerSerializer(user)
        serialized_data = user_serializer.data
        serialized_data["token"] = str(token)
        serialized_data["phone_number"] = serializer.data['phone_number']
        return Response(serialized_data)



class StoreView(APIView):
    authentication_classes = (TokenAuthentication, )
    
    def post(self, request):
        user = Token.objects.get(key=request.META['HTTP_AUTHORIZATION'].split(' ')[1]).user
        data = request.data
        user = Account.objects.get(username=user.username)
        
        print(data['address'])
        store = Store.objects.create(store_name=data['store_name'], address=data['address'], owner=user)
        path = "https://"+data['address']   
        data = {"store_id": store.id, "store-link": path+"/"+store.slug+"/"}
        return HttpResponse(json.dumps(data),content_type='application/json')


class ProductAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    def post(self, request):
        data = request.data
        print(data)
        serializer = ProductSerializer(data=data)      
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        data = {"id": serializer.data['id'], 'name': serializer.data['product_name'], "image": serializer.data['image']}
        return HttpResponse(json.dumps(data), content_type='application/json')
