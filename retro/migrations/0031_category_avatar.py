# Generated by Django 3.2.19 on 2023-07-20 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retro', '0030_auto_20230719_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='avatar',
            field=models.CharField(default='default-category.png', max_length=60),
        ),
    ]
