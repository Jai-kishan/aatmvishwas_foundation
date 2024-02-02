import os
import sys

#### initiation of cron script ####

print("Init")

#### setup django environment to user django models ####
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foundation.settings")
import django

django.setup()
from apps.models import *
from django.core.files import File

team = TeamMember.objects.filter()

image_path = '/home/jai/Downloads/jai_kishan.jpg'
team_details = [
    {
        "name": "Annu Bharti",
        "title": "Mrs",
        "image": "/home/jai/Downloads/jai_kishan.jpg",
        "bio": "developer",
        "address": "Uttam Nagar Delhi",
        "position": "Techincal Assistant",
        "social_media": "",
        "age": 25,
    },
        {
        "name": "Chandni Kumari",
        "title": "Mrs",
        "image": "",
        "bio": "Changemakers like Chandni can really be a game changer for local development. She is committed, humble, learning-oriented, knows what she is up against and still ready to be a doer!",
        "address": "Uttam Nagar Delhi",
        "position": "Co-Founder",
        "social_media": "",
        "age": 25,
    },
    {
        "name": "Anuradha",
        "title": "Mrs",
        "image": "",
        "bio": "developer",
        "address": "Uttam Nagar Delhi",
        "position": "Administrative Assistant",
        "social_media": "",
        "age": 25,
    },
    {
        "name": "Vijay Kumar Paswan",
        "title": "Mr",
        "image": "",
        "bio": "developer",
        "address": "Uttam Nagar Delhi",
        "position": "Founder",
        "social_media": "",
        "age": 25,
    },
    {
        "name": "Prakash",
        "title": "Mr",
        "image": "",
        "bio": "developer",
        "address": "Uttam Nagar Delhi",
        "position": "Research associate",
        "social_media": "",
        "age": 25,
    },
    {
        "name": "Abodh Kumar",
        "title": "Mr",
        "image": "",
        "bio": "A Local leader who is a good Public relations specialist, and grater advisor",
        "address": "Uttam Nagar Delhi",
        "position": "Advisor",
        "social_media": "",
        "age": 25,
    },
]

for data in team_details:
    instance = TeamMember.objects.create(
        name=data.get("name"),
        title=data.get("title"),
        biography=data.get("bio"),
        address=data.get("address"),
        position=data.get("position"),
        social_media_link=data.get("social_media"),
        age=data.get("age"),
    )
    instance.image.save(f'{data.get("name")}.{image_path.split(".")[-1]}', File(open(image_path, 'rb')))

