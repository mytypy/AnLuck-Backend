from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    like = serializers.BooleanField()
    
    class Meta:
        model = Like
        fields = ('post', 'like')
    
    def create(self, validated_data):
        user = self.context['request'].user
        post = validated_data['post']
        
        return Like.objects.create(author=user, post=post)