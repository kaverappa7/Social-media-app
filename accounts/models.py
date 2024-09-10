from django.db import models
from django.contrib.auth.models import User


class Follow(models.Model):
    follower =  models.ForeignKey(User, on_delete=models.CASCADE,related_name="following")
    following =  models.ForeignKey(User, on_delete=models.CASCADE,related_name="followers")

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"  