from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

# 
router =  DefaultRouter()
# product 라는 이름으로 등록을 시켜줌.
router.register('product', views.ProductViewSet)

urlpatterns = [
    # 이렇게 리스트 형식으로 넣어줌. 
    path('', include(router.urls),
        )
    
]



