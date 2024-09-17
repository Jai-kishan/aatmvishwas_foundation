from django.db import models
from datetime import datetime
from PIL import Image
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
    biography = models.TextField()
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


class Program(models.Model):
    program_brief = models.ForeignKey('ProgramHeading', on_delete=models.CASCADE, related_name='program_heading')
    tagline = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    full_description = models.TextField()
    image = models.ImageField(upload_to='programs')
    short_desc_url = models.URLField(max_length=200, blank=True)
    full_desc_url = models.URLField(max_length=200, blank=True)
    key_points = models.TextField(blank=True, help_text="Enter key points separated by commas")
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    date_created_timestamp = models.CharField(max_length=50, blank=True)
    date_modified = models.DateTimeField(default=datetime.now, blank=True)
    date_modified_timestamp = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

    def get_key_points(self):
        if self.key_points:
            return [point.strip() for point in self.key_points.split(',')]
        return []

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # First save to generate image file
        if self.image:
            image_path = self.image.path  # Get the image file path
            img = Image.open(image_path)

            # Set the target dimensions
            target_width = 4080
            target_height = 3072

            # Resize the image to 1920x1080 (force resize, not keeping aspect ratio)
            img = img.resize((target_width, target_height), Image.ANTIALIAS)

            # Save the resized image back to the same path
            img.save(image_path)


    class Meta:
        verbose_name_plural  = "Program"
        db_table = 'program'

        

# class KeyPoint(models.Model):
#     banner = models.ForeignKey('Program', on_delete=models.CASCADE, related_name='key_points')
#     text = models.CharField(max_length=255)

#     def __str__(self):
#         return self.text
    

class ProgramHeading(models.Model):
    tag_line = models.CharField(max_length=255)
    heading = models.CharField(max_length=255)
    overview = models.TextField()

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name_plural  = "Program Heading"
        db_table = 'program_heading'