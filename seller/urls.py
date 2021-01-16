
from django.contrib import admin
from django.urls import path, include
from .views import OwnerSignUpAPIView, StoreView, ProductAPIView
urlpatterns = [
    path('signup/', OwnerSignUpAPIView.as_view()),
    path('store/', StoreView.as_view()),
    path('product/', ProductAPIView.as_view())
]
