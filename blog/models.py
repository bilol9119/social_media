from django.db import models
from authorization.models import MyUser


class Post(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='posts/')

    def __str__(self):
        return self.user.user.username


class Comment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.user.user.first_name


class Like(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Follow(models.Model):
    following = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='follower')


