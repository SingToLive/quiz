from rest_framework import serializers
from .models import Category as CategoryModel
from .models import Item as ItemModel
from .models import Order as OrderModel
from .models import ItemOrder as ItemOrderModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['name']
        
class ItemSerializer(serializers.ModelSerializer):
    category = serializers.SerilalizerMethodField()
    
    class Meta:
        model = ItemModel
        fields = ['name', 'category', 'image_url']
        
class OrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=True, read_only=True)
    
    class Meta:
        models = OrderModel
        fields = ['delivery_address', 'order_date', 'item']
        
class ItemSeiralizer(serializers.ModelSerializer):
    item = ItemSerializer(many=True)
    order = OrderSerializer(many=True)
    
    class Meta:
        models = ItemModel
        fields = ['order', 'item', 'item_count']        