from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Customer, Item, Order, OrderItem, Cart, Payment
from .serializers import (
    CustomerSerializer,
    ItemSerializer,
    OrderSerializer,
    OrderItemSerializer,
    CartSerializer,
    PaymentSerializer,
)

def home(request):
    return render(request, 'home.html')

def customers(request):
    return render(request, 'customers.html')

def items(request):
    return render(request, 'items.html')

def orders(request):
    return render(request, 'orders.html')

def order_items(request):
    return render(request, 'order-items.html')

def payments(request):
    return render(request, 'payments.html')

def cart(request):
    return render(request, 'cart.html')


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        order_id = request.data.get('order')
        order_items = OrderItem.objects.filter(order_id=order_id)

        total_amount = sum(item.item.price * item.quantity for item in order_items)

        serializer = self.get_serializer(data={
            'amount': total_amount,
            'order': order_id
        })
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)