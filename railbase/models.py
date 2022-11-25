from django.db import models

# Create your models here.
class File(models.Model):
    title = models.TextField()
    file = models.FileField(upload_to='images/')

    def __str__(self):
        return self.title