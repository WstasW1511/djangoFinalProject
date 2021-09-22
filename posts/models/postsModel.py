from django.db import models
from users.models import CustomUser
from utils.models import  AbstractUUID, AbstractTimeTracker
from utils.const import ViewChoise


class Posts(AbstractUUID, AbstractTimeTracker):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст поста', max_length=1000)
    moderate = models.BooleanField(blank=True, null=True)
    view = models.CharField(choices=ViewChoise.choice(), max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return str(self.text)
