# Generated by Django 4.2.11 on 2024-10-01 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.CharField(choices=[('aatmvishwas center', 'Aatmvishwas Center'), ('community', 'Community Engagement'), ('student_life', 'Student Life'), ('events', 'Events & Functions')], max_length=20),
        ),
    ]