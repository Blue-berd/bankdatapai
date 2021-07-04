from .models import Banks, Branches
from rest_framework import serializers
from rest_framework import viewsets

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields= ['name', 'id']

class BranchSerializer(serializers.ModelSerializer):
    bank = BankSerializer(read_only=True)
    class Meta:
        model = Branches
        fields= ['ifsc','bank','branch','address','city','district','state']
        extra_kwargs = {
            'bank': {'allow_null': True, 'required': False},   
        }
