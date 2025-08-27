from django.http import HttpRequest
from django.db.models import Count, Prefetch
from rest_framework.viewsets import ViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from User.models import User
from Comments.models import Comment
from .models import Post, PostImage
from .serializer import PostSerializer, PostViewSerializer


class PostReadOnlyModelViewSet(ReadOnlyModelViewSet): # Если в таких классах есть кастомный action, то нужно самому вызывать get_queryset
    permission_classes = (IsAuthenticated, )
    serializer_class = PostSerializer
    
    def get_queryset(self):
        qs = (
            Post.objects
            .select_related('author')
            .annotate(comment_count=Count('commentary_post', distinct=True))
            .prefetch_related(
                Prefetch('post_image', queryset=PostImage.objects.order_by('order'), to_attr='post_image_prefetch'),
                Prefetch(
                    'commentary_post',
                    queryset=Comment.objects.filter(parent__isnull=True).select_related('author').prefetch_related(
                        Prefetch('replies', queryset=Comment.objects.select_related('author'), to_attr='replies_prefetch')
                    ),
                    to_attr='top_comments_prefetch'
                )
            ).order_by('-created_at')
        )

        user_tag = self.request.GET.get('user')
        
        if user_tag:
            qs = qs.filter(author__tag=user_tag)
            
        return qs
    
    @action(
        methods=['GET'],
        detail=False
    )
    def posts(self, request: HttpRequest):
        posts = self.get_queryset()
        serializer = self.get_serializer(posts, many=True)
        
        return Response(serializer.data)


class PostViewSet(ViewSet):
    serializer_class = PostViewSerializer
    permission_classes = (IsAuthenticated, )
    
    @action(
        methods=['POST'],
        detail=False
    )
    def add_post(self, request: HttpRequest):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({'response': 'Запись успешно создана!'})