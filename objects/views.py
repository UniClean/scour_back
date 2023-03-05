from rest_framework import generics
from .serializers import ObjectSerializer, ObjectCreateSerializer
from .models import Object
from rest_framework.response import Response
from rest_framework import status


class ObjectList(generics.ListCreateAPIView):
    queryset = Object.objects.filter(deleted=False)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ObjectSerializer
        elif self.request.method == 'POST':
            return ObjectCreateSerializer
        else:
            return ObjectSerializer

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


class ObjectDetail(generics.RetrieveAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
    lookup_field = 'id'


class ObjectUpdate(generics.UpdateAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectCreateSerializer
    lookup_field = 'id'


class ObjectDestroy(generics.DestroyAPIView):
    queryset = Object.objects.all()
    lookup_field = 'id'
