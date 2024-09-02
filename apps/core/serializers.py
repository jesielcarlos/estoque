from rest_framework import serializers
from apps.core.models import (
    Category,
    Product,
    StockMovement
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields = ("id", "name")


class ProductSerializerList(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    class Meta:
        model= Product
        fields = (
            "id", 
            "name",
            "description","price",
            "stock_quantity",
            "category"
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields = (
            "id", 
            "name",
            "description",
            "price",
            "stock_quantity",
            "category"
        )


class StockMovementSerializerList(serializers.ModelSerializer):
    product = ProductSerializer(many=False)
    class Meta:
        model= StockMovement
        fields = (
            "id",
            "product",
            "movement_type",
            "quantity",
            "reason",
            "created_at"
        )


class StockMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model= StockMovement
        fields = (
            "id",
            "product",
            "movement_type",
            "quantity",
            "reason",
            "created_at"
        )
