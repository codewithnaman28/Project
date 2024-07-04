# templates/views.py

from rest_framework import viewsets
from django.http import HttpResponse
from .models import Template
from .serializers import TemplateSerializer

class TemplateViewSet(viewsets.ModelViewSet):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

def home(request):
    return HttpResponse("Welcome to the SymphonyTech Assignment!")
