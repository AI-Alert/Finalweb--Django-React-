from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vollclub.urls', namespace='vollclub')),
    path('api/', include('vollclub_api.urls', namespace='vollclub_api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
