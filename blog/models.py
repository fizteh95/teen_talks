from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    content = RichTextField()
    preview = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
