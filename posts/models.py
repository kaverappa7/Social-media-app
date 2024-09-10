from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to="post_images/",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return f"{self.author.username} : {self.content[:30]}..."



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return f"{self.author.username} on {self.post} : {self.content[:30]}..."



class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} liked {self.post}"
    


