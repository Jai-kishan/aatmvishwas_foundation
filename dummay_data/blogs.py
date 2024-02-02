import os
import sys
from datetime import datetime

#### initiation of cron script ####

print("Init")

#### setup django environment to user django models ####
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foundation.settings")
import django

django.setup()
from apps.models import *
from django.core.files import File
from django.utils import timezone

current_datetime = timezone.now()

team = Blog.objects.filter()

image_path = "static/assets/images/events/image_{}.jpg"
blogs = [
    {
        "title": "Methods of Recuirtments",
        "author": "Jai",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam justo neque, aliquet sit amet elementum vel, vehicula eget eros. Vivamus arcu metus, mattis sed sagittis at, sagittis quis neque. Praesent.",       
        "date_created_timestamp": datetime.now().timestamp(),
    },
    {
        "title": "Education",
        "author": "Jai",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam justo neque, aliquet sit amet elementum vel, vehicula eget eros. Vivamus arcu metus, mattis sed sagittis at, sagittis quis neque. Praesent.",       
        "date_created_timestamp": datetime.now().timestamp(),
    },
    {
        "title": "How to Become a Rich",
        "author": "Jai",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam justo neque, aliquet sit amet elementum vel, vehicula eget eros. Vivamus arcu metus, mattis sed sagittis at, sagittis quis neque. Praesent.",       
        "date_created_timestamp": datetime.now().timestamp(),
    },
    {
        "title": "Billionaires in India",
        "author": "Jai",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam justo neque, aliquet sit amet elementum vel, vehicula eget eros. Vivamus arcu metus, mattis sed sagittis at, sagittis quis neque. Praesent.",       
        "date_created_timestamp": datetime.now().timestamp(),
    },
    {
        "title": "Life of Software Engineer",
        "author": "Jai",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam justo neque, aliquet sit amet elementum vel, vehicula eget eros. Vivamus arcu metus, mattis sed sagittis at, sagittis quis neque. Praesent.",       
        "date_created_timestamp": datetime.now().timestamp(),
    },
    {
        "title": "Rich Data & Poor Dad",
        "author": "Jai",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam justo neque, aliquet sit amet elementum vel, vehicula eget eros. Vivamus arcu metus, mattis sed sagittis at, sagittis quis neque. Praesent.",       
        "date_created_timestamp": datetime.now().timestamp(),
    },
    {
        "title": "Mom is Just WOW!!",
        "author": "Jai",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam justo neque, aliquet sit amet elementum vel, vehicula eget eros. Vivamus arcu metus, mattis sed sagittis at, sagittis quis neque. Praesent.",       
        "date_created_timestamp": datetime.now().timestamp(),
    },
    {
        "title": "Methods of Recuirtments",
        "author": "Jai",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam justo neque, aliquet sit amet elementum vel, vehicula eget eros. Vivamus arcu metus, mattis sed sagittis at, sagittis quis neque. Praesent.",       
        "date_created_timestamp": datetime.now().timestamp(),
    },
]

for count, data in enumerate(blogs):
    image_path= f"static/assets/images/events/image_0{count+1}.jpg"
    instance = Blog.objects.create(
        title=data.get("title"),
        author=data.get("author"),
        content=data.get("content"),
        date_published=current_datetime,
        date_created=current_datetime,
        date_modified=current_datetime,
        date_created_timestamp=data.get("date_created_timestamp"),
    )
    instance.image.save(
        f'{data.get("title")}.{image_path.split(".")[-1]}', File(open(image_path, "rb"))
    )
