# Generated by Django 3.1.3 on 2020-11-08 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConfManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
