from django.db import models
from utils.models import AbstractUUID, AbstractTimeTracker
from .postsModel import Posts
from users.models import CustomUser
from utils.const import Likes


class Like(AbstractUUID, AbstractTimeTracker):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    kind = models.CharField(choices=Likes.choice(), max_length=50)
    # created_at = models.DateField(auto_now_add=True)
    # updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'

    def __str__(self):
        return str(self.kind)

