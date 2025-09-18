from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CommentaryViewSet


router = SimpleRouter()
router.register(prefix=r'comments', viewset=CommentaryViewSet, basename='commentary')


urlpatterns = [
    path('api/', include(router.urls))
]