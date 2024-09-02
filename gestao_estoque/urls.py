from django.contrib import admin
from django.urls import path, include
import apps.core.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(apps.core.urls, namespace="api")),
]
