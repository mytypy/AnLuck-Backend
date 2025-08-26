from rest_framework import serializers
from .models import Comment
from utils.utils import normal_time


class CommentarySerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()
    time = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'time', 'avatar', 'replies')
        
    def get_author(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name or ''}".strip()
    
    def get_avatar(self, obj):
        request = self.context.get('request')
        avatar = getattr(obj.author, 'avatar', None)
        
        if not avatar:
            return None
        
        url = avatar.url if hasattr(avatar, 'url') else str(avatar)
        return request.build_absolute_uri(url) if request else url

    def get_time(self, obj):
        return normal_time(obj.created_at)

    def get_replies(self, obj):
        replies_qs = getattr(obj, 'replies_prefetch', None) or obj.replies.all()
        serializer = CommentarySerializer(replies_qs, many=True, context=self.context)
        return serializer.data