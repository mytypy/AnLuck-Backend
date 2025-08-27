from rest_framework import serializers
from ..models import User
from django.contrib.auth.base_user import BaseUserManager


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'password', 'email')
    
    def validate_email(self, value):
        manager = BaseUserManager()
        email = manager.normalize_email(email=value)
        exist = User.objects.filter(email=email).exists()
        
        if exist:
            raise serializers.ValidationError('Пользователь с таким email уже существует')
        
        return value
    
    def validate_first_name(self, value):
        
        if len(value) < 2:
            raise serializers.ValidationError('Имя должно быть больше одной буквы')
        
        return value
    
    def validate_last_name(self, value):
        
        if len(value) < 1:
            raise serializers.ValidationError('Фамилия должна содержать минимум 1 букву')
        
        return value
    
    def validate_password(self, value):
        
        if len(value) < 8:
            raise serializers.ValidationError('Пароль должен быть минимум из 8 символов')
        
        return value
        
    def create(self, validated_data):
        validated_data['tag'] = f'user_{User.objects.count() + 1}'
        return User.objects.create_user(**validated_data)