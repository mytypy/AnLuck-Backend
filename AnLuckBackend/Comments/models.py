from django.db import models


class Comment(models.Model):
    author = models.ForeignKey('User.User', on_delete=models.CASCADE, related_name='user_comment')
    post = models.ForeignKey('Posts.Post', on_delete=models.CASCADE, related_name='commentary_post')
    text = models.TextField('Текст комментария', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('Comments.Comment', on_delete=models.CASCADE, related_name='parent_comment')
