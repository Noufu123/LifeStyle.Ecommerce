# Generated by Django 4.1.2 on 2022-11-17 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_lifestyle', '0028_alter_ordermodel_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='payment_id',
            field=models.CharField(blank=True, default='1000000000000', max_length=500, null=True),
        ),
    ]
