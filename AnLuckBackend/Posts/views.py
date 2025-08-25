from django.http import HttpRequest
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class PostViewSet(ViewSet):
    permission_classes = (IsAuthenticated, )
    
    @action(
        methods=['GET'],
        detail=False
    )
    def posts(self, request: HttpRequest):
        return Response([
    {
      'id': 1,
      'author': "Никита Григорьев",
      'text': "Just finished an amazing photoshoot in the mountains! The golden hour lighting was absolutely perfect. Can't wait to share the results with you all! 📸✨",
      'time': "2 hours ago",
      'avatar': "https://avatars.githubusercontent.com/u/143941740?v=4",
      'image': "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/image-KEkt9WNlawOqMoSiy5DAnjFlWoAH9H.png",
      'likes': 42,
      'comments': 8,
      'shares': 3,
      'commentsList': [
        {
          'id': 1,
          'author': "Анна",
          'text': "Потрясающие фотографии! 😍",
          'time': "1 hour ago",
          'avatar': "/diverse-female-avatar.png",
          'replies': [
            {
              'id': 11,
              'author': "Никита Тик Ток",
              'text': "Спасибо большое! ❤️",
              'time': "30 min ago",
              'avatar': "https://avatars.githubusercontent.com/u/143941740?v=4",
            },
          ],
        },
        {
          'id': 2,
          'author': "Максим",
          'text': "Золотой час действительно волшебный",
          'time': "45 min ago",
          'avatar': "/diverse-female-avatar.png",
          'replies': [],
        },
      ],
    }
  ])