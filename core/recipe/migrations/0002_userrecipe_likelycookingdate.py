# Generated by Django 4.2.7 on 2024-01-01 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrecipe',
            name='likelyCookingDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
