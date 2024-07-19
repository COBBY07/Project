from django.db import models
from .validators import file_size

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(upload_to="video/%y", validators=[file_size])
    
    def __str__(self):
        return self.title