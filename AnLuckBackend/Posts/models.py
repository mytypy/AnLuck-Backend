from django.db import models


class Post(models.Model):
    name = models.TextField('Запись пользователя', blank=False)
    author_id = models.ForeignKey('User.User', on_delete=models.CASCADE, related_name='post')
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.BigIntegerField('Лайки', blank=False, default=0)
    shares = models.BigIntegerField('Шейры', blank=False, default=0)
    # update_at = Добавить позже


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_image')
    file_url = models.ImageField('Путь до файла', upload_to="images/")
    order = models.IntegerField('Порядок в посте', blank=False)
    created_at = models.DateTimeField(auto_now_add=True)