from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Item, Feedback
from .serializers import ItemSerializer, FeedbackSerializer


class PostPagePagination(PageNumberPagination):
    page_size = 10


class ItemViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    API для получения списка товаров
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'category', 'available']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_date', 'price']
    pagination_class = PostPagePagination


class FeedbackViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    API для создания и получения отзывов
    """
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    pagination_class = PostPagePagination

