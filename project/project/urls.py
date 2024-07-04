from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from templates.views import TemplateViewSet, home

router = DefaultRouter()
router.register(r'templates', TemplateViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', home),  # Add this line for the home view
]
