# Generated by Django 4.1.2 on 2022-11-17 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_lifestyle', '0030_orderitemmodel_user_forgn_alter_ordermodel_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitemmodel',
            name='user_forgn',
        ),
    ]