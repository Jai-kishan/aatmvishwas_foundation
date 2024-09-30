import os
import django
#import ipdb
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "foundation.settings"
)  # nirla is the name of the project
django.setup()

from apps.models import *
from banner.models import Banner
from django.utils import timezone  # Import timezone
import time
from datetime import datetime


blog_data = [
    {
        "title": "Students studing by their own in the campus premises",
        "author": "PK",
        "content": "Our campus library boasts over 1,000 books, creating an environment that encourages students to develop a love for reading and self-study. We foster a study culture where students immerse themselves in learning, exploring diverse subjects independently. By providing ample resources and a supportive atmosphere, we empower our students to take charge of their education and cultivate lifelong learning habits.",
        "image": "blogs/center-1.png",
        "date_published": timezone.now(),  
        "date_created_timestamp": int(time.time()),
         
    },
    {
        "title": "Community Awareness Event among villagers.",
        "author": "PK",
        "content": "Our NGO recently held a community awareness program for adults and seniors, emphasizing the importance of educating their children, maintaining hygiene, and understanding government schemes. We also highlighted vaccination programs. These sessions aimed to empower our community with vital knowledge, ensuring a healthier and more informed future for everyone. Together, we can build a stronger, educated, and healthier community.",
        "image": "blogs/community-1.png", 
        "date_published": timezone.now(), 
        "date_created_timestamp": int(time.time()),
        
    },
    {
        "title": "Community Engagement with agenda how to keep village clean",
        "author": "PK",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laudantium hic consequatur beatae architecto,",
        "image": "blogs/center-4.png",  
        "date_published": timezone.now(),
        "date_created_timestamp": int(time.time()),
        
    },
    {
        "title": "Recuirtments in Saajhe Sapne",
        "author": "PK",
        "content": "Today, a meeting was convened jointly by the 'Atmasvishwas Foundation' and 'Saajhe Sapne' in Harira Panchayat, Araria district. The focus of the discussion was on advancing opportunities for girls and exploring collaborative efforts to support them in achieving their aspirations. Following the meeting, all girls who had applied for 'Saajhe Sapne' underwent examinations, with each demonstrating commendable performance and crafting their future strategies. Together with Jyoti ji, representing the 'Atmasvishwas Foundation', we facilitated a conducive environment for the girls to excel in their exams. The girls from our community are now filled with pride having participated in the 'Saajhe Sapne' examination. The knowledge and skills they acquired today are truly invaluable. We remain optimistic that through the collective efforts of 'Saajhe Sapne' and the 'Atmasvishwas Foundation', the girls in our area will be empowered to realize their dreams.",
        "image": "blogs/center-2.png",  
        "date_published": timezone.now(),
        "date_created_timestamp": int(time.time()),
        
    },
    {
        "title": "Extra Curricular Activity",
        "author": "PK",
        "content": "At our NGO, we complement formal education with extra curricular activities such as drawing, poetry recitation, and dancing. These activities enhance creativity and confidence, providing a all-rounded development for our students. By integrating arts and academics, we ensure our students grow into well-balanced, talented individuals ready for diverse challenges.",
        "image": "blogs/fun-activities-1.png",  
        "date_published": timezone.now(),
        "date_created_timestamp": int(time.time()),
        
    },
    {
        "title": "Personal Hygiene",
        "author": "PK",
        "content": "Today, we organized our first weekly class at the Aatmvishwas Foundation Centre, marking the beginning of our new tradition of hosting unique activity sessions with the children every Saturday.During today's session, we focused on personal hygiene by checking the children's nails. Those with overgrown nails had them trimmed, and we also conducted checks on their teeth and clothing. Moving forward, this activity will take place every Saturday to instill a sense of cleanliness and neatness among the children.",
        "image": "blogs/personalHygiene-read-less.png",
        "date_published":timezone.now(),
        "date_created_timestamp": int(time.time()),

    },
    {
        "title": "Importance of mutual Growth",
        "author": "PK",
        "content": "Ayush and Harsh joined Atmasvishwas Foundation as volunteers on January 9th for a month, excelling the learning journey of our students and bonding with them. They made significant contributions to our NGO. They received farewell gifts and a work experience certificate. Their dedication was appreciated, and they intend to stay engaged with the foundation. Heartfelt farewells concluded their impactful stint.",
        "image": "blogs/center-1.png",
        "date_published":timezone.now(), 
        "date_created_timestamp": int(time.time()),
        
    },
    {
        "title": "Regular excercise for physical well-being",
        "author": "PK",
        "content": "In the early morning, guided by our volunteer Santoli Ji, our students walk through the fields of the village, breathing in the fresh, pure air. They begin their day with a morning walk in the lush greenery, followed by exercises that fill them with positive energy. They play various outdoor games, learning discipline and teamwork along the way.",
        "image": "blogs/exercise-read-less.png",
        "date_published":timezone.now(),  
        "date_created_timestamp": int(time.time()),
        
    },
    {
        "title": "Explaning about sanje sapne residential program",
        "author": "PK",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laudantium hic consequatur beatae architecto,",
        "image": "blogs/community-4.png",
        "date_published":timezone.now(),
        "date_created_timestamp": int(time.time()),
        
    }

]    

for blog in blog_data:
    Blog.objects.create(
        title=blog.get("title"),
        author=blog.get("author"),
        content=blog.get("content"),
        image=blog.get("image"),
        date_published=blog.get("date_published"),
        date_created_timestamp=blog.get("date_created_timestamp"),
        
    )
print("Blog entries created successfully!")

