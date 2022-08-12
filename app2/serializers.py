from rest_framework import serializers
from app2.models import CustomerData

class CSerializer(serializers.ModelSerializer):
    class Meta:
        model =   CustomerData
        fields = ('id' , 'username' , 'phone_no' , 'dob', 'email' , 'product' , 'dop')
