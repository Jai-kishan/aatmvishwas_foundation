import os
import django
#import ipdb
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "foundation.settings"
)  # nirla is the name of the project
django.setup()

from apps.models import *
from banner.models import Banner
import time
from datetime import datetime


team_member_data = [
    {
        "name": "Vijay Kumar Paswan",
        "position": "Founder",
        "bio": "I am originally from Katihar and have been residing in Araria since 2010. My journey in the social sector began in 2010 with Jan Jagran Shakti Sangathan, where I spent nearly a decade organizing communities and advocating for their rights.In July 2021, I joined Project Potential organization for 18 months. Inspired by my experiences, I co-founded the Aatmvishwas Foundation in July 2022 in Amgachhi Panchayat, Sikti block, Araria district. Our Aatmvishwas Center provides free education and fosters youth development.Concurrently, I completed my graduation and plan to pursue a Master of Social Work. Through the Aatmvishwas Foundation, I aim to drive positive change in society. I'm working directly at the grassroots level with our beneficiaries, including children, youth, and senior citizens.",
        "image": "team/vijay.png",
        "date_created_timestamp": int(time.time()),
    },
    {
        "name": "Chandni Kumari",
        "position": "Co-Founder",
        "bio": "I joined Jan Jagran Shakti Sangathan (JJSS) in 2013, immersing myself in various social initiatives. During a 2015 fellowship, I interned at JJSS, teaching children and organizing sports in villages. In 2016, I joined the Narmada Bachao Andolan in Madhya Pradesh, understanding grassroots struggles. I also worked with Project Potential, using drama for community engagement, and Charm organization, empowering women with internet literacy. In 2018. Later, in Saharsa, I continued with JJSS, teaching children through sports and advocating for rights. Drawing from these experiences, I co-founded the Aatmvishwas Foundation Center in my hometown, emphasizing basic education and youth development. Additionally, I pursue the Jeevt Fellowship project with Project Potential in the School of Programming, aiming to positively impact society through education and empowerment.",
        "image": "team/chand7.png",
        "date_created_timestamp": int(time.time()),
    },
    {
        "name": "Abodh Kumar",
        "position": "Mentor And Advisor",
        "bio": "Abodh Ji is a humble, kind, and lifelong learner dedicated to bringing positive change to the community. With a deep love for theater, he aims to provide employment and career opportunities to around 1 lakh youth, driven by his ultimate dream of seeing others achieve their dreams through his work, showcasing his selfless dedication and vision for a brighter future. Ha has a Postgraduate Diploma in Leadership Development from Azim Premji University, Bengaluru and his drive toward personal development and community impact has led him to lead all our community activities and bring key on-ground insights to our strategic decisions. With 20 years in the development sector and as Co-Founder of NGO Project Potential, Abodh's leadership drives impactful community activities and provides valuable field insights. He helps our organization grow by expanding networks, diversifying funding, and strengthening our mission. Abodh is a true inspiration, guiding our path to growth and amplifying our community impact.",
        "image": "team/abodh.png",
        "date_created_timestamp": int(time.time()),
    },
    {
        "name": "Annu Bharti",
        "position": "Trustee & Co-Founder",
        "bio": "I was born and raised in the culturally vibrant town of Kishanganj, Bihar, where I completed my schooling. My journey transformed when I became an alumna of two NGOs, Project Potential and Navgurukul Organisation, positively impacting me, my family, and my community.I am grateful to the social workers who transformed my life, inspiring me to uplift my community. Professionally, I am a self-taught Software Engineer with five years in the tech industry, using my skills to make meaningful contributions.I have a soft corner for the social sector and a strong curiosity to work for women empowerment. Despite my professional pursuits, my heart remains in the social sector, where I am fervently involved in empowering marginalized communities.Annu inspires girls to build their careers and lives, sharing her journey at Josh Talks, while balancing professional and social sector work to develop rural communities through educational and employment initiatives.",
        "image": "team/a6.png",
        "date_created_timestamp": int(time.time()),
    },
    {
        "name": "Anuradha",
        "position": "Trustee & Co-Founder",
        "bio": "Originally from Bihar and raised in Delhi, I completed my schooling and graduation in Delhi. My passion lies in education and women's empowerment. Currently, I'm fully engaged in Teach For India as a teaching fellow (2022-2024 cohort), embracing challenges while fostering creativity and strength.I worked at Alohomora Education Foundation as a community lead fellow, facilitating the Careershala program and assisting high school students to explore different career opportunities. I find joy in exploration, meaningful conversations, and connecting with new people. With over 5 years in the social sector.I've served as a Community Lead fellow, guiding students to find interest-aligned career paths.As a Teach For India fellow, I prioritize holistic learning and development among primary-grade students, aspiring to make a meaningful impact on society.",
        "image": "team/anu.png",
        "date_created_timestamp": int(time.time()),
    },
    {
        "name": "Santoli Kumari",
        "position": "Santoli Kumari",
        "bio": "Santoli Kumari, a beacon of inspiration hailing from the village of Makhdumpur, Jehanabad, Bihar, has illuminated the path for countless girls in her community. Her remarkable journey began with a dedication to education, culminating in her completion of 10+2 in 2020. Eager to further her skills, Santoli enrolled in a Project Management course offered by Shared Dreams, a program under the auspices of Sajhe Sapne NGO, dedicated to empowering rural women with career-oriented education.With a steadfast commitment to personal and professional growth, Santoli's journey has been marked by significant milestones. Following her educational pursuits, she spent a transformative year with Billion Readers, where she honed her skills and broadened her horizons.Presently, she serves as a teacher at the Aatmvishwas Foundation, embodying her passion for education and community development. Santoli's unwavering dedication and determination position her as a promising and influential figure, inspiring others to pursue their dreams and make meaningful contributions to society.",
        "image": "team/Santoli.png",
        "date_created_timestamp": int(time.time()),
    },
    {
        "name": "Parkash Sahu",
        "position": "Parkash Sahu",
        "bio": "He is, an intrepid explorer hailing from Chhattisgarh, has dedicated the past two years to immersing himself in the realm of social development. With an insatiable curiosity, he traverses through various NGOs' events, seeking to understand and contribute to causes close to his heart. His journey in the social sector is not just a profession but a personal quest for meaning and connection.In his quest for understanding, he seeks solace in life's simple moments, often taking walks to connect with nature and others. He cherishes sharing meals, discussing Hindi literature, and engaging in casual conversations, finding value in shared experiences. With diverse interests ranging from gender issues to psychedelics, he eagerly engages with a variety of perspectives, reflecting his passion for exploration and connection.Passionate and empathetic, he actively seeks opportunities to engage with individuals and communities, eager to learn from their unique stories and experiences. His ability to blend personal connection with intellectual inquiry makes him invaluable for any team striving for social change and collective understanding.",
        "image": "team/Prakash.png",
        "date_created_timestamp": int(time.time()),
    },
    {
        "name": "Yogendra Chaubey",
        "position": "Advisor",
        "bio": "Experienced and accomplished professional with a decade of dedicated service in India's Public Education System. Expert in consulting with Government School Headmasters and teachers, providing valuable guidance on leadership competencies. Proven track record of delivering successful teacher capacity building workshops.Skilled in community outreach, stakeholder relationship building, communication, and management. Proficient in monitoring fellowship programs and evaluating academic leadership initiatives. In-depth knowledge of education tools to enhance child learning outcomes.Vast experience in strengthening school processes, including library development and innovative learning opportunities. Passionate about creating new avenues for learning in government schools. A driven professional contributing to the advancement of education.",
        "image": "team/Yogendra Choubey.png",
        "date_created_timestamp": int(time.time()),
    },
    {
        "name": "Shravan Kumar Jha",
        "position": "Advisor",
        "bio": "Shravan Kumar Jha, Co-Founder and Chief Knowledge Officer (CKO) of i-Saksham, holds an MBA from Symbiosis, Pune, and has over 12 years of experience in Women’s Financial Inclusion, Gender, Government flagship schemes, and Education.Before founding i-Saksham in 2015, Shravan worked in the microfinance sector for four years and served as a Prime Minister Rural Development Fellow (PMRDF) for three and a half years, contributing significantly to rural development.Recognized as an Acumen Fellow in 2016, Shravan’s dedication and leadership in social change continue to inspire and guide our mission. His expertise and commitment make him an invaluable advisor to our organization.",
        "image": "team/Shravan Kumar Jha.png",
        "date_created_timestamp": int(time.time()),
    },
    {
        "name": "Krishna",
        "position": "Advisor",
        "bio": "Krishna leads Bihar operations and government liaison at Youth Dreamers Foundation (YDF). With a master’s in Rural Management and Development from Patna University, he brings strategic insights and local expertise. His deep commitment to Bihar and past role as a hospital administrator underscore his dedication to sustainable development.Born and raised in Bihar, Krishna's personal connection fuels his mission to empower communities through YDF's initiatives. His leadership is proactive and driven by a passion for positive change. Krishna's blend of professional acumen and personal drive makes him a dynamic force in YDF's efforts to empower Bihar's youth.Krishna's leadership style is enriched by interests in sports and travel, reflecting his holistic approach to community development. His strategic vision and hands-on experience drive YDF's mission, making impactful contributions to Bihar's socio-economic landscape.",
        "image": "team/Krishna.png",
        "date_created_timestamp": int(time.time()),
    }
    
]

for member in team_member_data:
    TeamMember.objects.create(
        name=member.get("name"),
        position=member.get("position"),
        bio=member.get("bio"),
        image=member.get("image"),
        date_created_timestamp=member.get("date_created_timestamp"),
    )