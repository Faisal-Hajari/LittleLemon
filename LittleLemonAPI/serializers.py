from rest_framework import serializers
from .models import MenuItem, Category
from decimal import Decimal

class CategorySerializers(serializers.ModelSerializer): 
    class Meta: 
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemSerializers(serializers.ModelSerializer): 
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category = CategorySerializers(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta: 
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory', 'price_after_tax', 'category', 'category_id']
    
    def calculate_tax(self, product:MenuItem): 
        return product.price * Decimal(1.1)