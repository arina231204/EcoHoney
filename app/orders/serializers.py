from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['first_name', "last_name", "email", "phone", 'delivery', "address", "city"]

    def validate(self, data):
        if not data['first_name'].isalpha():
            raise serializers.ValidationError('Недопустимые символы!')
        if not data['last_name'].isalpha():
            raise serializers.ValidationError('Недопустимые символы!')
        return data

