from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpRequest
from .serializers import CommentarySetSerializer


class CommentaryViewSet(ViewSet):
    serializer_class = CommentarySetSerializer
    
    @action(
        methods=['POST'],
        detail=False
    )
    def set_comment(self, request: HttpRequest):
        serializer = self.serializer_class(data=request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({'response': 'Ok!'})
