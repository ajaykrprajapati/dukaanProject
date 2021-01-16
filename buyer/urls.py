from django.urls import path
from .views import StoreDetailsAPIView, ProductDetails, CartItemsAPIView, OrderAPIView

urlpatterns = [
    path("store_details/", StoreDetailsAPIView.as_view()),
    path("product_details/", ProductDetails.as_view()),
    path("cart_details/", CartItemsAPIView.as_view()),
    path("order/<int:pk>/", OrderAPIView.as_view()),
]
