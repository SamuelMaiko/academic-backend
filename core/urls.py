from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('secret-route/', admin.site.urls),
    path('api/',include('api.urls')),
]
