# Generated by Django 3.2.7 on 2021-09-28 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210928_1607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='social_youtube',
            new_name='social_website',
        ),
    ]
