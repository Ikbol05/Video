from django.db import models

# Create your models here.



class Video(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='videos/')
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
