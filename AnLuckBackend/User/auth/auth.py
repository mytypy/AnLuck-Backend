from rest_framework_simplejwt.views import TokenObtainPairView
from .cookies import set_cookies
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.http import HttpRequest
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.decorators import action


class CookieTokenObtainPairView(TokenObtainPairView):
    
    serializer_class = TokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs) # Получаем объект Response

        if response.status_code == 200:
            access_token = response.data.get('access')
            refresh_token = response.data.get('refresh')
            
            if access_token and refresh_token:
                response = set_cookies(response, access_token, refresh_token) # Ставим http-only cookie в headers
                del response.data['access']
                del response.data['refresh']

        return response


class RegistrationViewSet(ViewSet):
    serializer_class = RegistrationSerializer
    
    @action(
        methods=['POST'],
        detail=False
    )
    def registration(self, request: HttpRequest):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'response': 'Регистрация прошла успешно!'})