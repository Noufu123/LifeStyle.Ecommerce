# Generated by Django 4.1.2 on 2022-10-31 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_lifestyle', '0012_delete_contact_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('message', models.TextField(max_length=1000)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
