# 파이썬 객체를 Json 형태로 변환하는 코드
# => 데이터베이스에 입력할 수 있도록 하기 위함

from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Product
        fields = (
            # init에 있는 fields를 가져옴
            
            'id',
            'product_name',
            'price',
            
        )


