# Generated by Django 3.2.4 on 2021-06-27 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_notes', '0002_auto_20210625_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]