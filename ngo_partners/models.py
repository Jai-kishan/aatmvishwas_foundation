from django.db import models
from PIL import Image, ImageDraw
import os

from datetime import datetime



# Create your models here.

class Partner (models.Model):
    name = models.CharField(max_length=100)
    discription = models.TextField()
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='partner/')
    star = models.IntegerField(default=5)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    date_created_timestamp = models.CharField(max_length=50, blank=True)
    date_modified = models.DateTimeField(default=datetime.now, blank=True)
    date_modified_timestamp = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save to generate image file
        if self.image:
            image_path = self.image.path  # Get the image file path
            img = Image.open(image_path)

            # Set the target dimensions
            target_size = (150, 150)  # Width, Height
            radius = 150  # Radius for rounded corners

            # Use Image.Resampling.LANCZOS for high-quality resizing
            img = img.resize((target_size[0], target_size[1]), Image.Resampling.LANCZOS)

            # Save the resized image back to the same path
            img.save(image_path)
