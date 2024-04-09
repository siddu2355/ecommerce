from rest_framework import serializers
from .models import Customer, Item, Order, OrderItem, Cart, Payment

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'customer_id', 'order_date']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order_item_id', 'order_id', 'item_id', 'quantity', 'price']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['cart_id', 'customer_id', 'quantity', 'item_id']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['payment_id', 'amount', 'order_id', 'payment_date']
