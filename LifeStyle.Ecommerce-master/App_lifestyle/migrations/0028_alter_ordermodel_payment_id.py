# Generated by Django 4.1.2 on 2022-11-17 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_lifestyle', '0027_remove_productmodel_meta_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='payment_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
