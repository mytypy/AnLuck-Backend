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
    first_name = models.CharField('Имя пользователя', max_length=40, blank=False)
    last_name = models.CharField('Фамилия пользователя', max_length=40, blank=True, null=True)
    tag = models.CharField('Тег пользователя', max_length=32, blank=True, null=True)
    email = models.EmailField('Email пользователя', unique=True, blank=False)
    bio = models.CharField('Описание профиля пользователя', max_length=128, blank=True, default='Не указано')
    location = models.CharField('Местоположение пользователя', max_length=32, blank=True, default='Не указано')
    website = models.URLField('Web-site пользователя', max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
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
            'name': f'{self.first_name} {self.last_name}',
            'tag': self.tag,
            'bio': self.bio,
            'location': self.location,
            'website': self.website,
            'joinDate': self.format_data(),
            'work': self.work,
            'avatar': self.avatar
        }