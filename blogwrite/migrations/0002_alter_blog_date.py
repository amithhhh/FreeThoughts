# Generated by Django 4.2.5 on 2023-12-27 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogwrite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
