# Generated by Django 4.2.7 on 2023-12-28 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eyeapp', '0017_blogcategory_alter_doctordetails_about_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.TextField(default='e'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
