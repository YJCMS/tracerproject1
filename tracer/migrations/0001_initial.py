# Generated by Django 4.0.3 on 2022-03-26 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
