# from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializer import ProductSerializer
from .models import Product

class ProductViewSet(ModelViewSet):
    # ModelViewSet을 상속받아서 ProductViewSet 클래스에서 
    # 모든 기능을 활용 가능함
    
    # 어떠한 모델에 대해서 다룰것인지, => object.all 하면 모든것을 다룸
    queryset = Product.objects.all()
    
    # 우리가 만들어뒀던 ProductSerializer 를 사용할 수 있음
    serializer_class = ProductSerializer



