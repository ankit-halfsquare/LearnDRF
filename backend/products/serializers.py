from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse



class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        # fields = '__all__'
        # fields = ['id', 'title', 'content','price', 'getDiscount','sale_price']
        fields = ['url','pk','title', 'content','price', 'discount','sale_price']

    
    def get_url(self, obj):
        # return f"/api/v2/product/{obj.pk}"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail",kwargs={'pk':obj.pk},request=request)

    def get_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None

        if not isinstance(obj, Product):
            return None
            
        try:
            return obj.getDiscount()
        except:
            return None
