from rest_framework.views import APIView
from django.http import HttpResponse
import json
from .serializers import CartSerializer, CustomerSerializer
from .models import Store, Product, Order, Cart, Customer, ItemDetail

# Create your views here.
from rest_framework.authtoken.models import Token

from django.db.models.query import QuerySet


class StoreDetailsAPIView(APIView):
    def post(self, request):
        data = request.data
        store_link = data["store_link"]
        store = Store.objects.filter(address=store_link)
        store = store[0]
        data = {
            "store_id": store.id,
            "store name": store.store_name,
            "address": store.address,
        }
        return HttpResponse(json.dumps(data), content_type="application/json")


# {"store_link": "http://127.0.0.1:8000/seller/store/store-1-3445/"}


class ProductDetails(APIView):
    def post(self, request):
        data = request.data
        store_link = data["store_link"]
        store = Store.objects.filter(address=store_link)
        store = store[0]
        query = Product.objects.filter(store=store).query
        query.group_by = ["category"]
        products = QuerySet(query=query, model=Product)
        data = list(products)
        return HttpResponse(data, content_type="application/json")


class CartItemsAPIView(APIView):
    """
        if pk of cart isnot  provided in the body, then a new cart is created,
        otherwise items are added to that cart
        for a given cart, if the product is already present then only the quantity is change
        otherwise the product is added to the cart or removed from the cart
    """

    serializer_class = CartSerializer

    def post(self, request):
        data = request.data
        print(data)
        if "pk" in request.data:
            cart = Cart.objects.get(id=data["pk"])
        else:
            cart = Cart.objects.create(store_link=data["store_link"])
        product_id = data["product_id"]
        quantity = data["quantity"]
        product = Product.objects.get(id=product_id)
        if ItemDetail.objects.filter(product=product, cart=cart):
            item = ItemDetail.objects.get(product=product, cart=cart)
            item.quantity = quantity
            item.save()
            if quantity == 0:
                item.delete()
        else:
            ItemDetail.objects.create(product=product, quantity=quantity, cart=cart)
        return HttpResponse(
            json.dumps({"data": "cart has been updated"}),
            content_type="application/json",
        )


class OrderAPIView(APIView):
    def post(self, request, pk):
        print(request.META["HTTP_AUTHORIZATION"])
        if "HTTP_AUTHORIZATION" in request.META:
            user = Token.objects.get(
                key=request.META["HTTP_AUTHORIZATION"].split(" ")[1]
            ).user
            print(user.username)
            try:
                user = Customer.objects.get(username=user.username)
            except Customer.DoesNotExist:
                if "phone_number" in request.data:
                    data = request.data
                    user = request.user
                    serializer = CustomerSerializer(data=data)
                    if serializer.is_valid():
                        print("valid")
                        serializer.save()
                    else:
                        print(serializer.errors)
                    user = Customer.objects.get(
                        username=serializer.data["phone_number"]
                    )
                    token, created = Token.objects.get_or_create(user=user)
                else:
                    return HttpResponse(
                        {"Kindly provide phone number or authorize using token"}
                    )
        elif "phone_number" in request.data:
            data = request.data
            user = request.user
            serializer = CustomerSerializer(data=data)
            if serializer.is_valid():
                print("valid")
                serializer.save()
            else:
                print(serializer.errors)
            user = Customer.objects.get(username=serializer.data["phone_number"])
            token, created = Token.objects.get_or_create(user=user)
        else:
            return HttpResponse(
                {"Kindly provide phone number or authorize using token"}
            )
        try:
            cart = Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return HttpResponse({"Empty cart"})
        order = Order.objects.create(cart=cart, customer=user)
        data = {"order_id": order.id}
        return HttpResponse(json.dumps(data), content_type="application/json")
