from django.shortcuts import redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Item
from .cart import Cart

from .serializers import CartSerializer


@api_view(['POST'])
def cart_add(request, product_id):
    """
        Добавление товара в корзину по ID.
    """
    cart = Cart(request)
    product = get_object_or_404(Item, id=product_id)
    cd = request.data
    try:
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    except KeyError:
        return Response("Не переданы данные")
    return redirect('cart_detail')


@api_view(['GET'])
def cart_remove(request, product_id):
    """
        Удаление товара из корзины по ID.
    """
    cart = Cart(request)
    product = get_object_or_404(Item, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


@api_view(['GET'])
def cart_clear(request):
    """
        Удаление корзины.
    """
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail')


@api_view(['GET'])
def cart_total_sum(request):
    """
        Получение полной стоимости всех товаров.
    """
    cart = Cart(request)
    return Response(cart.get_total_price())


@api_view(['GET'])
def cart_count(request):
    """
        Получение количества всех товаров.
    """
    cart = Cart(request)
    return Response(len(cart))


@api_view(['GET'])
def cart_detail(request):
    """
        Получение списка всех товаров в корзине.
    """
    cart = Cart(request)
    dict_ser = CartSerializer(cart, many=True)
    return Response(dict_ser.data)



