# Generated by Django 3.2.4 on 2021-06-25 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='notes',
            name='note',
            field=models.TextField(),
        ),
    ]
