# Generated by Django 5.0 on 2024-02-02 10:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apps", "0006_remove_contactus_timestamp_remove_donateus_timestamp_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teammember",
            name="biography",
            field=models.TextField(max_length=250),
        ),
    ]
