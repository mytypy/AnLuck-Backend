from django.http import HttpRequest
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer


class UserViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    
    @action(
        methods=['GET'],
        detail=False
    )
    def user(self, request: HttpRequest):
        serializer = self.serializer_class(request.user.me, context={'request': request})
        
        return Response({'user': serializer.data})
