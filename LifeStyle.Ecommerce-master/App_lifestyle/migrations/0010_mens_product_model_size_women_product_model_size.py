# Generated by Django 4.1.2 on 2022-10-30 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_lifestyle', '0009_alter_accessories_model_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mens_product_model',
            name='Size',
            field=models.CharField(default='M', max_length=55),
        ),
        migrations.AddField(
            model_name='women_product_model',
            name='Size',
            field=models.CharField(default='M', max_length=55),
        ),
    ]