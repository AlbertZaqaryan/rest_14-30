from rest_framework import serializers
from .models import Phone

class PhoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'