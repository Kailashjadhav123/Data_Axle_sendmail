from rest_framework import serializers
from email_.models import Employee, Template


class Employee_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("__all__",)



class Template_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ("__all__",)