# Generated by Django 4.0.5 on 2022-10-22 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_lifestyle', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_registration_model',
            name='status',
        ),
    ]