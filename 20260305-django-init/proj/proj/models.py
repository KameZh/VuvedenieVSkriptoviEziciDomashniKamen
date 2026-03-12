from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField()
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title