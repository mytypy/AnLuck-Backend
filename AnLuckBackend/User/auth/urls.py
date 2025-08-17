from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .login import CookieTokenObtainPairView



urlpatterns = [
    path('api/token/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]