# Generated by Django 3.2.19 on 2023-07-25 20:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('retro', '0034_remove_article_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='rating',
            field=models.ManyToManyField(blank=True, related_name='article_rating', to=settings.AUTH_USER_MODEL),
        ),
    ]
