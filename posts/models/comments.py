from django.db import models
from utils.models import AbstractUUID, AbstractTimeTracker
from  posts.models import Posts
from users.models import CustomUser


class CommentModel(AbstractUUID, AbstractTimeTracker):
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE, verbose_name='Пост', related_name='comment')
    comment = models.CharField(max_length=100, verbose_name='Комментарий')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Автор поста')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    #parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return str(self.posts)

