from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpRequest
from .serializers import CommentarySetSerializer, CommentarySetReplySerializer


class CommentaryViewSet(ViewSet):
    serializer_class_set = CommentarySetSerializer
    serializer_class_reply = CommentarySetReplySerializer
    permission_classes = (IsAuthenticated, )
    
    @action(
        methods=['POST'],
        detail=False
    )
    def set_comment(self, request: HttpRequest):
        serializer = self.serializer_class_set(data=request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        result = serializer.save()

        return Response({'response': result.pk})
    
    @action(
        methods=['POST'],
        detail=False
    )
    def reply_commentary(self, request: HttpRequest):
        serializer = self.serializer_class_reply(data=request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        result = serializer.save()

        return Response({'response': result.pk})