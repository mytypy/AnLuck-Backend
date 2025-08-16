from django.http import HttpRequest
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(ViewSet):
    
    @action(
        methods=['GET'],
        detail=False
    )
    def user(self, request: HttpRequest):
        return Response({'response': f'Ваши данные в GET: {request.GET}'})