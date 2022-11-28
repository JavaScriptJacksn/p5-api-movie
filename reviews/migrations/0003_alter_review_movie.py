# Generated by Django 3.2.16 on 2022-11-28 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20221124_1535'),
        ('reviews', '0002_rename_author_review_editor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie.movie'),
        ),
    ]
