from rest_framework import generics
from .serializers import EmployeeSerializer, EmployeeCreateSerializer, PositionSerializer, PositionCreateSerializer
from .models import Employee, Position
from rest_framework.response import Response
from rest_framework import status


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EmployeeSerializer
        elif self.request.method == 'POST':
            return EmployeeCreateSerializer
        else:
            return EmployeeSerializer

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


class PositionList(generics.ListCreateAPIView):
    queryset = Position.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PositionSerializer
        elif self.request.method == 'POST':
            return PositionCreateSerializer
        else:
            return PositionSerializer

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