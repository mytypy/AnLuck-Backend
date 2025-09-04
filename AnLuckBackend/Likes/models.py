from django.db import models


class Like(models.Model):
    author = models.ForeignKey('User.User', on_delete=models.CASCADE, related_name='user_like')
    post = models.ForeignKey('Posts.Post', on_delete=models.CASCADE, related_name='like_post')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = (('author', 'post'), )