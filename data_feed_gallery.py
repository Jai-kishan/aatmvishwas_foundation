import os
import django
#import ipdb
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "foundation.settings"
)  # nirla is the name of the project
django.setup()
from apps.models import Photo


photos_data = [
    {
        'title': 'Aatmvishwas Foundation Center',
        'image': 'gallery_photos/aatm-text-in-hindi.jpg',
        'category': 'aatmvishwas center',
    },
    {
        'title': 'Mediation Practice',
        'image': 'gallery_photos/meditation.jpg',
        'category': 'aatmvishwas center',
    },
    {
        'title': 'Students in Campus',
        'image': 'gallery_photos/girls-in-campus.png',
        'category': 'aatmvishwas center',
    },
    {
        'title': 'Photo in campus',
        'image': 'gallery_photos/savitri-phule.jpg',
        'category': 'aatmvishwas center',
    },
    {
        'title': 'Our Center',
        'image': 'gallery_photos/our-center.png',
        'category': 'aatmvishwas center',
    },
    {
        'title': 'Volunteer Visit',
        'image': 'gallery_photos/volunteers.png',
        'category': 'aatmvishwas center',
    },
    {
        'title': 'Center',
        'image': 'gallery_photos/center-1.jpg',
        'category': 'aatmvishwas center',
    },
    {
        'title': 'Campus',
        'image': 'gallery_photos/center-2.jpg',
        'category': 'aatmvishwas center',
    },
    {
        'title': 'Academic Excellence',
        'image': 'gallery_photos/center-3.jpg',
        'category': 'aatmvishwas center',
    },
    {
        'title': 'Kids in Our Campus',
        'image': 'gallery_photos/kids-in-campus.jpg',
        'category': 'aatmvishwas center',
    },
    {
        'title': 'Welcome to Aatmvishwas Foundation',
        'image': 'gallery_photos/welcome.jpg',
        'category': 'aatmvishwas center',
    },
    {
        'title': 'Nails Checking',
        'image': 'gallery_photos/nail-checking.jpg',
        'category': 'community',
    },
    {
        'title': 'Students with team members',
        'image': 'gallery_photos/kids-with-annu.png',
        'category': 'community',
    },
    {
        'title': 'Students with team members',
        'image': 'gallery_photos/community-1.jpg',
        'category': 'community',
    },
    {
        'title': 'Students with team members',
        'image': 'gallery_photos/community-2.jpg',
        'category': 'community',
    },
    {
        'title': 'Students with team members',
        'image': 'gallery_photos/community-3.jpg',
        'category': 'community',
    },
    {
        'title': 'Students with team members',
        'image': 'gallery_photos/community-4.png',
        'category': 'community',
    },
    {
        'title': 'Students with team members',
        'image': 'gallery_photos/community-IMG.jpg',
        'category': 'community',
    },
    {
        'title': 'Students with team members',
        'image': 'gallery_photos/carom.png',
        'category': 'community',
    },
    {
        'title': 'Students playing Carom Game',
        'image': 'gallery_photos/stud-power.jpg',
        'category': 'student_life',
    },
    {
        'title': 'Students playing Carom Game',
        'image': 'gallery_photos/fun-activities-1.png',
        'category': 'student_life',
    },
    {
        'title': 'Students playing Carom Game',
        'image': 'gallery_photos/playing.png',
        'category': 'student_life',
    },
    {
        'title': 'Annerversary Celebration Of Vijay And Chandni Ji',
        'image': 'gallery_photos/anner-celebration.jpg',
        'category': 'events',
    },
    {
        'title': 'Farewell of Volunteers',
        'image': 'gallery_photos/events-1.jpg',
        'category': 'events',
    },
    {
        'title': 'Independence Day Celebration',
        'image': 'gallery_photos/event-3.jpg',
        'category': 'events',
    },
    {
        'title': 'Drawing Competition',
        'image': 'gallery_photos/fun-activities-1.png',
        'category': 'events',
    },
    {
        'title': 'Volunteers Visit',
        'image': 'gallery_photos/banner.png',
        'category': 'events',
    },
    {
        'title': 'Facililatior Taking Class',
        'image': 'gallery_photos/event-2.png',
        'category': 'events',
    },
    {
        'title': 'Morning Exercise',
        'image': 'gallery_photos/fun-exercise.png',
        'category': 'events',
    },
    {
        'title': 'Personal Hygiene',
        'image': 'gallery_photos/nail-checking_N9jC2eE.jpg',
        'category': 'events',
    },
    {
        'title': 'Youth',
        'image': 'gallery_photos/youths.png',
        'category': 'events',
    },

]

for photo_data in photos_data:
    Photo.objects.get_or_create(
        title=photo_data['title'],
        image=photo_data['image'],
        category=photo_data['category'],
    )

print("gallery photos entered successfully!")