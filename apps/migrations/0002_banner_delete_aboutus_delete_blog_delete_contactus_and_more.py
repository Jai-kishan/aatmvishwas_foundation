# Generated by Django 4.2.7 on 2023-11-27 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='home')),
                ('url', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='AboutUs',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='ContactUs',
        ),
        migrations.DeleteModel(
            name='DonateUs',
        ),
        migrations.DeleteModel(
            name='Home',
        ),
        migrations.DeleteModel(
            name='TeamMember',
        ),
    ]
