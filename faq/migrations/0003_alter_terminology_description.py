# Generated by Django 3.2.19 on 2023-07-13 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0002_alter_terminology_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminology',
            name='description',
            field=models.CharField(max_length=3000),
        ),
    ]
