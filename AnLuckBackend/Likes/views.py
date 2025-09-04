from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpRequest
from .serializer import LikeSerializer
from .models import Like


class LikeViewSet(ViewSet):
    serializer_class = LikeSerializer
    
    @action(
        methods=['POST'],
        detail=False
    )
    def add_like(self, request: HttpRequest):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        like = Like.objects.filter(post=data['post'])
        
        if like.exists():
            like.delete()
        else:
            serializer.save()
        
        return Response({'response': 'Like'})