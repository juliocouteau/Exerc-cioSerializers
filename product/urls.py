from django.urls import path, include
from rest_framework import routers
from product import views # Importa as views do seu app product

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]