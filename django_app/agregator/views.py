from django.shortcuts import render

from .models import Product, MeasureUnit, Category
from .serializers import ProductSerializer, MeasureUnitSerializer, CategorySerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

class MainView(viewsets.ModelViewSet):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        serializer = self.get_serializer(instance = self.get_queryset(), many = True)
        return Response(serializer.data)
    
    """
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)"""