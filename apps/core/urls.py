from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.core.views import (
    ProductViewSet,
    StockMovementViewSet
)


router = DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"movements", StockMovementViewSet)
app_name = "core"
urlpatterns = [
    path("", include(router.urls)),
]

