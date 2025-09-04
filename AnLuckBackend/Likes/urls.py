from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import LikeViewSet


router = SimpleRouter()
router.register(prefix=r'like', viewset=LikeViewSet, basename='like')


urlpatterns = [
    path('api/', include(router.urls))
]