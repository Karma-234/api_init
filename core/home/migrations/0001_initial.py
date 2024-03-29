# Generated by Django 4.2.7 on 2023-12-31 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField(default=18)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('file', models.FileField(upload_to='')),
                ('streetName', models.TextField(blank=True, null=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('createdAt', models.DateTimeField()),
                ('key', models.UUIDField(unique=True)),
            ],
        ),
    ]
