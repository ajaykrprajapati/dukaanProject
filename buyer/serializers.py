from .models import Product, Customer, ItemDetail, Cart
from rest_framework import serializers
from seller.serializers import CategorySerializer
from seller.models import Category

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta():
        model = Product
        fields = ['id', 'product_name', 'description', 'mrp', 'sales_price', 'image', 'category', 'store']

    def create(self, validated_data):
        print(validated_data['category'])
        c, _ = Category.objects.get_or_create(name=validated_data['category']['name'])
        validated_data.pop('category')
        validated_data.update({'category': c})
        product = Product.objects.create(**validated_data)
        return product

class ItemDetailsSerializer(serializers.ModelSerializer):

    class Meta():
        model = ItemDetail
        fields = ['product', 'quantity', 'cart']
    

class CartSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cart
        fields = ['store_link']
    

class CustomerSerializer(serializers.ModelSerializer):
    otp = serializers.CharField(max_length=5, read_only=True)
    phone_number = serializers.CharField(source='username')
    class Meta():
        model = Customer
        fields = ['otp', 'phone_number', 'address']

    def validate(self, attrs):
        attrs.update({'password': ''})
        return attrs


