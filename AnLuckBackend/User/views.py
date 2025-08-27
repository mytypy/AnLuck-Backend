from django.http import HttpRequest
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer, UserUpdateSerializer


class UserViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)
    user_serializer_class = UserSerializer
    update_serializer_class = UserUpdateSerializer
    
    @action(
        methods=['GET'],
        detail=False
    )
    def user(self, request: HttpRequest):
        serializer = self.user_serializer_class(request.user.me, context={'request': request})
        
        return Response({'user': serializer.data})
    
    @action(
        methods=['PATCH'],
        detail=False
    )
    def update_user(self, request: HttpRequest):
        serializer = self.update_serializer_class(instance=request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'response': serializer.validated_data})
