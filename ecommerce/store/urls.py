from django.urls import path
from . import views

urlpatterns = [
    #we will leave empty string for the base url
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout")
]