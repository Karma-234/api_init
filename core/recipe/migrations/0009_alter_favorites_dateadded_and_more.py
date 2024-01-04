# Generated by Django 4.2.7 on 2024-01-04 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0008_favorites_delete_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorites',
            name='dateAdded',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='favorites',
            name='favoriteRecipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipe.userrecipe'),
        ),
        migrations.AlterUniqueTogether(
            name='favorites',
            unique_together={('user', 'favoriteRecipe', 'dateAdded')},
        ),
    ]