from django.db import models

# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='home')
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title
