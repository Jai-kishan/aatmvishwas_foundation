from django.db import models
from datetime import datetime
from django.utils import timezone

import time


# Create your models here.
class Banner(models.Model):
    tag = models.CharField(max_length=25)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="slider")
    created_ts=models.DateTimeField(default=int(time.time()))
    modified_ts=models.DateTimeField(default=int(time.time()))
    link = models.URLField(blank=True, null=True)
    active = models.BooleanField(default=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.title()

    def is_active(self):
        """Check if the banner is active based on the current date and active status."""
        now = timezone.now()
        if self.active and (self.start_date <= now) and (self.end_date is None or self.end_date >= now):
            return True
        return False    

    class Meta:
        verbose_name_plural  = "Banner"
        db_table = 'banners'