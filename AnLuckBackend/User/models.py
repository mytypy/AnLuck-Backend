from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    
    def create_user(self, first_name, password, email, **params):
        email = self.normalize_email(email)
        user = self.model(first_name=first_name, email=email, **params)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    
class User(AbstractBaseUser):
    first_name = models.CharField('Имя пользователя', max_length=40, blank=False)
    last_name = models.CharField('Фамилия пользователя', max_length=40, blank=True)
    tag = models.CharField(max_length=32, blank=True)
    email = models.EmailField('Email пользователя', unique=True, blank=False)

    USERNAME_FIELD = 'email'
    
    objects = CustomUserManager()
    
    @property
    def me(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'tag': self.tag if self.tag else 'Не указано',
        }