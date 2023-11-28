from django.db import models

# Create your models here.

class Home(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='home')

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/images/about_us')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural  = "About Us"


class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team_members')
    biography = models.TextField()
    address = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    social_media_link = models.URLField()
    age = models.IntegerField()

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content  = models.TextField()
    image = models.ImageField(upload_to='blog')
    date_published = models.DateTimeField()

    def __str__(self):
        return self.title


class DonateUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    donation_amount = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    phone_number = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='home')
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title
