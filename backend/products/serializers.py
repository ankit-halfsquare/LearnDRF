from rest_framework import serializers
from .models import Product



class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        # fields = '__all__'
        # fields = ['id', 'title', 'content','price', 'getDiscount','sale_price']
        fields = ['id', 'title', 'content','price', 'discount','sale_price']

    
    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None

        if not isinstance(obj, Product):
            return None
            
        try:
            return obj.getDiscount()
        except:
            return None
