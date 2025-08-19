from django.urls import path, include
from .auth import CookieTokenObtainPairView, RegistrationViewSet
from .refresh_token import CookieTokenRefreshView
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(prefix=r'auth', viewset=RegistrationViewSet, basename='register')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/login/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
]