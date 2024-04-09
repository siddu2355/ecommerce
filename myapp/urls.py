from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CustomerViewSet,
    ItemViewSet,
    OrderViewSet,
    OrderItemViewSet,
    CartViewSet,
    PaymentViewSet,
)

router = DefaultRouter()
router.register('customers', CustomerViewSet)
router.register('items', ItemViewSet)
router.register('orders', OrderViewSet)
router.register('order-items', OrderItemViewSet)
router.register('cart', CartViewSet)
router.register('payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
