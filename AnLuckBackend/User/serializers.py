from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    name = serializers.CharField()
    tag = serializers.CharField()
    bio = serializers.CharField()
    location = serializers.CharField()
    website = serializers.URLField()
    joinDate = serializers.CharField()
    work = serializers.CharField()
    avatar = serializers.ImageField()
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)

        if not rep.get('website'):
            rep['website'] = 'http://null.dev'
        
        if not rep.get('tag'):
            rep['tag'] = 'Не указано'
            
        return rep