from rest_framework import serializers
from .models import Order
from objects.serializers import ObjectSerializer


class OrderSerializer(serializers.ModelSerializer):
    object = ObjectSerializer(source='object_id', many=False, read_only=True)

    class Meta:
        model = Order
        exclude = ('object_id',)
        depth = 1


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['object_id', 'type', 'additional_information',]