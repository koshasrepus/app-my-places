from django.db import models

class User(models.Model):
    """Пользователь Telegram"""
    chat_id = models.IntegerField()
    step = models.IntegerField()


class Palaces(models.Model):
    """Места"""
    title = models.CharField(max_length=100, default=None)
    place_lat = models.FloatField(default=None)
    place_lon = models.FloatField(default=None)
    image = models.ImageField()
    user = models.ForeignKey('User', on_delete=models.CASCADE)