from django.db import models
from django.conf import settings


class Blog(models.Model):
    submitter = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    blog = models.ForeignKey('blog.Blog', on_delete=models.CASCADE, related_name="posts")
    likers = models.ManyToManyField('auth.User')
    body = models.TextField()
    name = models.TextField()

    def __str__(self):
        return "Post '%s' on '%s'" % (self.name, self.blog.name)


class PostComment(models.Model):
    submitter = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()

    def __str__(self):
        return "Comment by User %s on Post '%s' by %s" % (
            self.submitter.username,
            self.post.name,
            self.post.blog.submitter.username,
        )
