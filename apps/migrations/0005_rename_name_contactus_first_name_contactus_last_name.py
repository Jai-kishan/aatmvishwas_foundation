# Generated by Django 5.0 on 2023-12-26 17:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apps", "0004_alter_banner_options_alter_contactus_options_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contactus",
            old_name="name",
            new_name="first_name",
        ),
        migrations.AddField(
            model_name="contactus",
            name="last_name",
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
