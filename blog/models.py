from django.db import models


class Post(models.Model):
    title = models.CharField(verbose_name='제목', max_length=100)
    content = models.TextField(verbose_name='내용')
    published_at = models.DateTimeField(verbose_name='발행일')

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]
