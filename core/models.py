from django.db import models

class User(models.Model):
    """Пользователь Telegram"""
    chat_id = models.IntegerField()
    step = models.IntegerField()


class Palaces(models.Model):
    """Места"""
    location = models
    image = models.ImageField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)