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

banners = Banner.objects.filter()


home_page_banners = [
    {
        "title": "BEST EDUCATION FOR DIPLOMA",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam justo neque, aliquet sit amet elementum vel, vehicula eget eros. Vivamus arcu metus, mattis sed sagittis at, sagittis quis neque. Praesent.",       
        "date_created_timestamp": datetime.now().timestamp(),
    },
    {
        "title": "YOU CAN HELP WITH THE POOR CHILDREN",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam justo neque, aliquet sit amet elementum vel, vehicula eget eros. Vivamus arcu metus, mattis sed sagittis at, sagittis quis neque. Praesent.",       
        "date_created_timestamp": datetime.now().timestamp(),
    },
    {
        "title": "How to Become a Rich",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam justo neque, aliquet sit amet elementum vel, vehicula eget eros. Vivamus arcu metus, mattis sed sagittis at, sagittis quis neque. Praesent.",       
        "date_created_timestamp": datetime.now().timestamp(),
    },
    {
        "title": "Billionaires in India",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam justo neque, aliquet sit amet elementum vel, vehicula eget eros. Vivamus arcu metus, mattis sed sagittis at, sagittis quis neque. Praesent.",       
        "date_created_timestamp": datetime.now().timestamp(),
    },
    {
        "title": "Life of Software Engineer",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam justo neque, aliquet sit amet elementum vel, vehicula eget eros. Vivamus arcu metus, mattis sed sagittis at, sagittis quis neque. Praesent.",       
        "date_created_timestamp": datetime.now().timestamp(),
    },
    {
        "title": "Rich Data & Poor Dad",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam justo neque, aliquet sit amet elementum vel, vehicula eget eros. Vivamus arcu metus, mattis sed sagittis at, sagittis quis neque. Praesent.",       
        "date_created_timestamp": datetime.now().timestamp(),
    },
    {
        "title": "Mom is Just WOW!!",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam justo neque, aliquet sit amet elementum vel, vehicula eget eros. Vivamus arcu metus, mattis sed sagittis at, sagittis quis neque. Praesent.",       
        "date_created_timestamp": datetime.now().timestamp(),
    },
    {
        "title": "Support Child for Education",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam justo neque, aliquet sit amet elementum vel, vehicula eget eros. Vivamus arcu metus, mattis sed sagittis at, sagittis quis neque. Praesent.",       
        "date_created_timestamp": datetime.now().timestamp(),
    },
]

for count, data in enumerate(home_page_banners):
    image_path= f"static/assets/images/slider/slider-{count+1}.jpg"
    instance = Banner.objects.create(
        title=data.get("title"),
        description=data.get("description"),
        date_created=current_datetime,
        date_modified=current_datetime,
        date_created_timestamp=data.get("date_created_timestamp"),
    )
    instance.image.save(
        f'slider-{count+1}.jpg', File(open(image_path, "rb"))
    )
