from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from .cookies import set_cookies


class CookieTokenRefreshView(TokenRefreshView):
    
    def post(self, request, *args, **kwargs):
        raw_refresh_token = request.COOKIES.get('refresh_token') or None
        
        data = {'refresh': raw_refresh_token}

        serializer = self.get_serializer(data=data)
        
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        
        response = Response(serializer.validated_data, status=200)
        
        access_token = response.data.get('access')
        refresh_token = response.data.get('refresh')
        
        if access_token and refresh_token:
            response = set_cookies(response=response, access=access_token, refresh=refresh_token)
            
            del response.data['access']
            del response.data['refresh']
        
        return response
