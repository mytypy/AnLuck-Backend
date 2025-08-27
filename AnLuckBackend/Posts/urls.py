from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PostReadOnlyModelViewSet, PostViewSet


router = SimpleRouter()
router.register(prefix=r'posts', viewset=PostReadOnlyModelViewSet, basename='posts')
router.register(prefix=r'post', viewset=PostViewSet, basename='post')


urlpatterns = [
    path('api/', include(router.urls)),

]