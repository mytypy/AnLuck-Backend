from django.http import HttpRequest
from rest_framework import serializers
from .models import Post, PostImage
from Comments.serializers import CommentarySerializer
from utils.utils import normal_time
        

class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True) # source - с какого атрибута брать
    author = serializers.SerializerMethodField()
    time = serializers.SerializerMethodField()
    avatar = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    comments = serializers.IntegerField(source='comment_count', read_only=True)
    commentsList = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ('id', 'time', 'author', 'text', 'shares', 'avatar', 'images', 'comments', 'commentsList', 'likes', 'is_liked')

    def get_normal_url(self, file_field):
        request: HttpRequest = self.context.get('request')
        url = file_field.url
        
        return request.build_absolute_uri(url)
        
    def get_author(self, obj):
        user = obj.author
        return f"{user.first_name} {user.last_name or ''}".strip()
    
    def get_time(self, obj):
        time = normal_time(obj.created_at)
        return time
    
    def get_avatar(self, obj):
        avatar_url = self.get_normal_url(obj.author.avatar)
        return avatar_url

    def get_images(self, obj):
        images = getattr(obj, 'post_image_prefetch', None)

        if not images:
            return None

        return [self.get_normal_url(i.file_url) for i in images]
    
    def get_commentsList(self, obj):
        top_comments = getattr(obj, 'top_comments_prefetch', None)
        
        if top_comments is None:
            top_comments = obj.commentary_post.filter(parent__isnull=True)
            
        serializer = CommentarySerializer(top_comments, many=True, context=self.context)
        
        return serializer.data
    
    def get_likes(self, obj):
        return obj.likes_count

    def get_is_liked(self, obj):
        return obj.is_liked
        
        
class PostViewSerializer(serializers.ModelSerializer):
    photos = serializers.ListField(
        child=serializers.FileField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Post
        fields = ('text', 'photos')

    def create(self, validated_data):
        user = self.context['request'].user
        files = validated_data.pop('photos', [])

        post = Post.objects.create(author=user, **validated_data)

        PostImage.objects.bulk_create([
            PostImage(post=post, file_url=f, order=i)
            for i, f in enumerate(files, start=1)
        ])

        return post