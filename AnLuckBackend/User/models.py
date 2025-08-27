from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from calendar import month_name


class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, password, email, **params):
        email = self.normalize_email(email)
        user = self.model(first_name=first_name, email=email, **params)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    first_name = models.CharField('Имя пользователя', max_length=40)
    last_name = models.CharField('Фамилия пользователя', max_length=40, blank=True, null=True)
    tag = models.CharField('Тег пользователя', max_length=32, unique=True, db_index=True)
    email = models.EmailField('Email пользователя', unique=True, db_index=True)
    bio = models.CharField('Описание профиля', max_length=128, blank=True, default='Не указано')
    location = models.CharField('Местоположение', max_length=32, blank=True, default='Не указано')
    website = models.URLField('Web-site', max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    work = models.CharField(max_length=20, blank=True, null=True, default='Не работает')
    avatar = models.ImageField(upload_to="images/", default="images/anonim.jpg")

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def format_data(self):
        date_obj = self.created_at
        month_number = date_obj.month
        month_name_str = month_name[month_number]
        return f'{date_obj.year} {month_name_str} {date_obj.day}'

    @property
    def me(self):
        return {
            'id': self.pk,
            'name': f'{self.first_name} {self.last_name}',
            'tag': self.tag,
            'bio': self.bio,
            'location': self.location,
            'website': self.website,
            'joinDate': self.format_data(),
            'work': self.work,
            'avatar': self.avatar
        }


class Chat(models.Model):
    name = models.CharField('Название чата', max_length=64, blank=True)
    is_group = models.BooleanField('Группа или нет', default=False, db_index=True)
    created_at = models.DateTimeField('Создан в:', auto_now_add=True)
    update_at = models.DateTimeField('Последний раз обновлен в:', auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['is_group']),
            models.Index(fields=['created_at']),
        ]


class ChatUser(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_users', verbose_name='Чат')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_chats', verbose_name='Пользователь')
    joined_at = models.DateTimeField('Вошёл в:', auto_now_add=True)

    class Meta:
        unique_together = ('chat', 'user')
        indexes = [
            models.Index(fields=['chat', 'user']),
        ]


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages', verbose_name='Чат', db_index=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages', verbose_name='Автор', db_index=True)
    text = models.TextField('Текст сообщения')
    send_at = models.DateTimeField('Создано в:', auto_now_add=True, db_index=True)

    class Meta:
        indexes = [
            models.Index(fields=['chat', 'send_at']),
            models.Index(fields=['user', 'send_at']),
        ]
