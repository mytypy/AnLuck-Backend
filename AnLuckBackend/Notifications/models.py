from django.db import models


class NotflicationTypes(models.TextChoices):
    NEW_MESSAGE = 'new_message', 'Новое сообщение'
    
    
class NotflicationType(models.Model):
    code = models.CharField('Короткий код', max_length=64, blank=False, choices=NotflicationTypes.choices)
    name = models.CharField('Человекочитаемое поле', max_length=64, blank=False)
    icon = models.ImageField(upload_to="images/")
    
    
class Notflication(models.Model):
    recipient = models.ForeignKey('User.User', on_delete=models.CASCADE, related_name='notflication')
    notification_type = models.ForeignKey(NotflicationType, on_delete=models.CASCADE, related_name='notflication_from_type')
    message = models.ForeignKey('User.Message', on_delete=models.CASCADE, related_name='notflication_message')
    post = models.ForeignKey('Posts.Post', on_delete=models.CASCADE, related_name='notflication_post')
    created_at = models.DateTimeField('Создано в:', auto_now_add=True)
    is_read = models.BooleanField('Прочитано ли сообщение', default=False)