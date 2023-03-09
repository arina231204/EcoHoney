from rest_framework import status, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import OrderItem, Order
from .serializers import OrderSerializer
from cart.cart import Cart


class OrderCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    API для создания заказов
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        cart = Cart(request)
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def order_paid(request, order_id):
    """
       Изменение статуса оплаты заказа по ID.
    """
    order = get_object_or_404(Order, id=order_id)
    if order.paid:
        return Response("Заказ уже оплачен!")
    else:
        order.paid = True
        order.save()
        return Response("Оплата принята!")


@api_view(['GET'])
def order_delivery(request, order_id):
    """
       Изменение статуса доставки заказа по ID.
    """
    order = get_object_or_404(Order, id=order_id)
    if order.delivery:
        order.paid = False
        order.save()
        return Response("Статус изменен на самовывоз")
    else:
        return Response("Статус уже самовывоз!")
