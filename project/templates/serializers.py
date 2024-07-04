from rest_framework import serializers
from .models import Template, Field

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'

class TemplateSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True)

    class Meta:
        model = Template
        fields = '__all__'

    def create(self, validated_data):
        fields_data = validated_data.pop('fields')
        template = Template.objects.create(**validated_data)
        for field_data in fields_data:
            Field.objects.create(template=template, **field_data)
        return template
