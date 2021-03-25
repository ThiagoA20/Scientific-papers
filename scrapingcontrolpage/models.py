from django.db import models

class papers(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.TextField()

    def __str__(self):
        return self.title
