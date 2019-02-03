from django.db import models

class Photo(models.Model):
    title = models.CharField(verbose_name='제목', max_length=100)
    image = models.ImageField(verbose_name='이미지', upload_to='images/')
    info = models.TextField(verbose_name='설명')

    def __str__(self):
        return self.title
