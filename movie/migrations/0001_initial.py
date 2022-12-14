# Generated by Django 3.2.16 on 2022-11-24 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('plot', models.TextField()),
                ('runtime', models.IntegerField()),
                ('rated', models.TextField()),
                ('poster', models.URLField()),
                ('title', models.TextField()),
                ('fullplot', models.TextField()),
                ('released', models.DateField()),
                ('lastupdated', models.DateField()),
                ('type', models.CharField(choices=[('UNRATED', 'Unrated'), ('TV-PG', 'TV-PG'), ('TV-G', 'TV-G')], default='UNRATED', max_length=7)),
            ],
        ),
    ]
