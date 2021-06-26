from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Browsable API Auth
    path('auth/', include('rest_framework.urls')),

    # App
    # path('', include('api.urls')),
]
