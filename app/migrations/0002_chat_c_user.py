# Generated by Django 4.0 on 2022-08-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='c_user',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
