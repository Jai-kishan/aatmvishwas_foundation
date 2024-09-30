import os
import django
import ipdb
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "foundation.settings"
)  # nirla is the name of the project
django.setup()

from apps.models import *
from banner.models import Banner
import time
from datetime import datetime


banner_data = [
    {
        "tag": "Our Learning Center",
        "title": "Every Child Deserves A Chance To Learn",
        "description": "Every child, regardless of their background or circumstances, deserves equal access to quality education, which is essential for unlocking their full potential and creating a brighter future.",
        "image": "slider/s1.png",
        "date_created_timestamp": int(time.time()),
    },
    {
        "tag": "Our Learning Center",
        "title": "Helping Hands Changing Future",
        "description": "Your support has the power to transform lives, offering hope and opportunities for a brighter future.",
        "image": "slider/s2.png",
        "date_created_timestamp": int(time.time()),
    },
    {
        "tag": "Our Learning Center",
        "title": "Lighting the Path: Empowering Youth Through Education and Employment",
        "description": "Empowering youth with education and employment opportunities, our NGO shines a light on promising tomorrows.",
        "image": "slider/Victory.jpg",
        "date_created_timestamp": int(time.time()),
    },
    {
        "tag": "Our Learning Center",
        "title": "Educating For A Brighter Tomorrow",
        "description": "By providing quality education today, we are nurturing a generation of empowered individuals who will create a brighter and more prosperous tomorrow for themselves and their communities.",
        "image": "slider/s3.png",
        "date_created_timestamp": int(time.time()),
    },
]

# for data in banner_data:
#     Banner.objects.create(
#         tag=data.get("tag"),
#         title=data.get("title"),
#         description=data.get("description"),
#         image=data.get("image"),
#         date_created_timestamp=data.get("date_created_timestamp"),
#     )


program_heading_obj = ProgramHeading.objects.get_or_create(
    tag_line="What We Do",
    heading="Our Rural Empowerment and Development Initiatives.",
    overview="Our Rural Empowerment and Development Initiatives aim to uplift rural communities by providing education, skill-building, and awareness programs. Through these initiatives, we strive to foster sustainable development and empower individuals with the tools and knowledge needed for socio-economic advancement. By focusing on education, skill development, and community engagement, we aim to create a positive impact that lasts for generations!",
)
# ipdb.set_trace()

program_data = [
    {
        "program_brief": program_heading_obj[0],
        "tagline": "Educating Childern Program",
        "title": "Seekho Aur Sikhao",
        "short_description": "Empowering rural communities through education and engagement, ensuring quality education and job skills for lifelong socio-economic advancement.",
        "full_description": "Empowering rural communities through education, guidance, and community engagement to foster lifelong learning and opportunities for socio-economic advancement, while ensuring every rural child gets quality education, youth learn skills for good jobs, and communities thrive together. Our NGO is dedicated to building the basics of students, strengthening their foundation, and fostering curiosity to learn. We believe in empowering students to study independently by clearing doubts and initating a passion for learning new things. Our programs aim to equip students with the skills and knowledge they need to succeed academically and in life. Join us in our mission to build a generation of strong, independent learners who are ready to take on the world!",
        "image": "program/first_program.jpg",
        "key_points": "Skilled Facilitator,Online Classes,Holistic Development,Enriches Confidence",
        "date_created_timestamp": int(time.time()),
    },
    {
        "program_brief": program_heading_obj[0],
        "tagline": "Youth Employment Program",
        "title": "Complete Your Dreams",
        "short_description": "We connects rural students with training centers for skills and job opportunities, empowering them and fostering community development.",
        "full_description": "Aatmvishwas Foundation serves as a transformative force, linking rural students with different NGO's training centers nationwide that offer skills and job opportunities. By bridging this gap, the organization empowers students from villages, equipping them with the necessary skills to secure meaningful employment. Through strategic partnerships with training centers, the NGO ensures that students gain access to quality education and job prospects, fostering a brighter future for these individuals and their communities.. Through its dedicated efforts, the NGO acts as a catalyst for socio-economic development, leveraging education and skill-building to uplift rural communities. By nurturing talent and fostering a culture of learning, it not only transforms individual lives but also contributes to the overall growth and prosperity of the nation. With a focus on empowerment and inclusivity, the NGO's work embodies the spirit of community-driven change, paving the way for a more equitable and prosperous society.",
        "image": "program/second_program.jpg",
        "key_points": "Youth Empowerment, Skill Building, Access to opportunities, Economic Growth",
        "date_created_timestamp": int(time.time()),
    },
    {
        "program_brief": program_heading_obj[0],
        "tagline": "Community Empowerment through Awareness",
        "title": "Awareness Campaigns",
        "short_description": "We organize regular programs in villages to educate and empower residents on social issues, fostering informed decision-making and community activism.",
        "full_description": "We organizes regular General Awareness programs in villages, focusing on critical social issues and agendas. These programs serve as platforms for educating villagers about topics such as health, sanitation, education, women's empowerment, and environmental conservation. Through interactive sessions, workshops, and awareness campaigns, the NGO aims to empower villagers with knowledge and information, enabling them to make informed decisions and improve their quality of life. By conducting these programs regularly, the NGO fosters a culture of awareness and activism within the community, encouraging villagers to actively participate in addressing social challenges. The programs not only educate villagers but also inspire them to take collective action, leading to positive changes in their lives and surroundings. Through these initiatives, the NGO plays a pivotal role in driving social change and promoting sustainable development in rural areas.",
        "image": "program/3rd_pro.png",
        "key_points": "Inclusivity, Grassroots initiatives, Community engagement, Rural upliftment",
        "date_created_timestamp": int(time.time()),
    },
]

for program in program_data:
    Program.objects.create(
        program_brief=program.get("program_brief"),
        tagline=program.get("tagline"),
        title=program.get("title"),
        short_description=program.get("short_description"),
        full_description=program.get("full_description"),
        image=program.get("image"),
        key_points=program.get("key_points"),
        date_created_timestamp=program.get("date_created_timestamp"),
    )
