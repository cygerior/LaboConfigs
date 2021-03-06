# Generated by Django 3.1.3 on 2020-11-08 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ConfManager', '0002_resource_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='labels',
            field=models.ManyToManyField(to='ConfManager.Label'),
        ),
    ]
