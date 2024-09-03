from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets

from apps.core.serializers import (
    ProductSerializer,
    ProductSerializerList,
    StockMovementSerializer,
    StockMovementSerializerList
)
from .models import (
    Product,
    StockMovement
)


class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        products = Product.objects.all().order_by("id")
        category = request.query_params.get("category", None)
        if category:
            products = products.filter(category=category)
        
        serializer = ProductSerializerList(products, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=400)

    def post(self, request):
        try:
            data = request.data
            serializer = ProductSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
        except Exception as e:
            return Response({'error': str(e)}, status=400)

    def partial_update(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=400)

    def destroy(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response(status=204)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class StockMovementViewSet(viewsets.ViewSet):
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer

    def list(self, request):
        product = request.query_params.get("product", None)
        input = request.query_params.get("input", None)
        stock_movements = StockMovement.objects.all().order_by("id")
        if product:
            stock_movements = stock_movements.filter(product=product)
        if input:
            stock_movements = stock_movements.filter(movement_type=input)
        
        serializer = StockMovementSerializerList(stock_movements, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            data = request.data
            product = data.get("product")
            movement_type = data.get("movement_type")
            quantity = data.get("quantity")
            product = Product.objects.get(pk=product)
            if movement_type == "IN":
                product.stock_quantity = product.stock_quantity + quantity
                product.save()
            elif movement_type == "OUT":
                product.stock_quantity = product.stock_quantity - quantity
                product.save()
            else:
                raise Exception("Invalid movement type")
            
            serializer = StockMovementSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
        except Exception as e:
            return Response({'error': str(e)}, status=400)
        