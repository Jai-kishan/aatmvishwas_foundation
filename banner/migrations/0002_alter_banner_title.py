# Generated by Django 5.0 on 2024-09-16 16:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("banner", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="banner",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]