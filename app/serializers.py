from rest_framework import serializers
from .models import Home

class HomeSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=222)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=222)
    phone = serializers.CharField(max_length=222)


    def create(self, validated_data):
        return Home.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance

    # field level Validation
    def validate_password(self, value):
        if len(value) <= 8:
            raise serializers.ValidationError('invalid password')
        return value

    #object level validation
    def validate(self, data):
        nm = data.get('username')
        ph = data.get('phone')
        if nm.lower() == 'rohit' and ph.lower() != '9810222916':
            raise serializers.ValidationError('phone num must be 9810222916')
        return data



