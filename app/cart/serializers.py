from rest_framework import serializers


class CartSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    product = serializers.CharField()
    product_id = serializers.IntegerField()
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2)