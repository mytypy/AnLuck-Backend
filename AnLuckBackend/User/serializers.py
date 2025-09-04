from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    tag = serializers.CharField()
    bio = serializers.CharField()
    location = serializers.CharField()
    website = serializers.URLField()
    joinDate = serializers.CharField()
    work = serializers.CharField()
    avatar = serializers.ImageField()
    posts = serializers.IntegerField()
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)

        if not rep.get('website'):
            rep['website'] = 'http://null.dev'
        
        if not rep.get('tag'):
            rep['tag'] = 'Не указано'
            
        return rep


class UserUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'tag', 'bio', 'location', 'website', 'work', 'avatar')
        
    def validate_tag(self, value):
        
        if len(value) < 4:
            raise serializers.ValidationError('Тег должен быть минимум из 4-х символов')
        
        return value
    
    def validate_first_name(self, value):
        
        if len(value) < 2:
            raise serializers.ValidationError('Имя должно быть больше одной буквы')
        
        return value
    
    def validate_last_name(self, value):
        
        if len(value) < 1:
            raise serializers.ValidationError('Фамилия должна содержать минимум 1 букву')
        
        return value