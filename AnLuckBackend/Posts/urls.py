from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PostViewSet


router = SimpleRouter()
router.register(prefix=r'post', viewset=PostViewSet, basename='post')


urlpatterns = [
    path('api/', include(router.urls))
]