from rest_framework import serializers
from .models import Category, MeasureUnit, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, required=False)
    measure_unit = MeasureUnitSerializer(many=False, required=False)
    class Meta:
        model = Product
        fields = '__all__'