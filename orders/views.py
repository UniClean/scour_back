from django.shortcuts import render

from rest_framework import generics
from .serializers import OrderSerializer, OrderCreateSerializer
from .models import Order
from rest_framework.response import Response
from rest_framework import status


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderSerializer
        elif self.request.method == 'POST':
            return OrderCreateSerializer
        else:
            return OrderSerializer

    def get(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        queryset = self.get_queryset()
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.


class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'