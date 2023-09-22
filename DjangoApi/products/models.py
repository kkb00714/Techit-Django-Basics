from django.db import models


class Product(models.Model):
    # 장고에서 지원하는 model을 상속해서 구현하도록 선언
    
    # CharField => 옵션을 주어서 문자열에 대한 제한을 둠
    product_name = models.CharField(max_length=30, blank=False, default='')
    
    # DecimalField => 부동소수점으로 표기됨
    price = models.DecimalField(max_digits=20, decimal_places=1, blank=False, default=0)
    
    # 
    


