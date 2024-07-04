from django.db import models

class Template(models.Model):
    name = models.CharField(max_length=100)

class Field(models.Model):
    template = models.ForeignKey(Template, related_name='fields', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    input_type = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
