# Generated by Django 4.0.3 on 2023-06-05 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_summury_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='user',
            field=models.IntegerField(default=0),
        ),
    ]
