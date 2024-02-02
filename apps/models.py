from django.db import models
from datetime import datetime
# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='home')
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    date_created_timestamp = models.CharField(max_length=50, blank=True)
    date_modified = models.DateTimeField(default=datetime.now, blank=True)
    date_modified_timestamp = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural  = "Home"
        db_table = 'home'
        


class AboutUs(models.Model):    
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/images/about_us')
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    date_created_timestamp = models.CharField(max_length=50, blank=True)
    date_modified = models.DateTimeField(default=datetime.now, blank=True)
    date_modified_timestamp = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural  = "About Us"
        db_table = 'about_us'


class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team_members')
    biography = models.TextField(max_length=250)
    address = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    social_media_link = models.URLField()
    age = models.IntegerField()
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    date_created_timestamp = models.CharField(max_length=50, blank=True)
    date_modified = models.DateTimeField(default=datetime.now, blank=True)
    date_modified_timestamp = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.title} {self.name}"

    class Meta:
        verbose_name_plural  = "Team Member"
        db_table = 'team_members'


class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content  = models.TextField()
    image = models.ImageField(upload_to='blog')
    date_published = models.DateTimeField()
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    date_created_timestamp = models.CharField(max_length=50, blank=True)
    date_modified = models.DateTimeField(default=datetime.now, blank=True)
    date_modified_timestamp = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blogs'

class DonateUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    donation_amount = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    date_created_timestamp = models.CharField(max_length=50, blank=True)
    date_modified = models.DateTimeField(default=datetime.now, blank=True)
    date_modified_timestamp = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural  = "Donate Us"
        db_table = 'donate_us'

class ContactUs(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    phone_number = models.CharField(max_length=10)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    date_created_timestamp = models.CharField(max_length=50, blank=True)
    date_modified = models.DateTimeField(default=datetime.now, blank=True)
    date_modified_timestamp = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name_plural  = "Contact Us"
        db_table = 'contact_us'


class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='home')
    url = models.URLField(max_length=200)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    date_created_timestamp = models.CharField(max_length=50, blank=True)
    date_modified = models.DateTimeField(default=datetime.now, blank=True)
    date_modified_timestamp = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural  = "Banner"
        db_table = 'banners'
        