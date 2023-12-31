# Generated by Django 4.1.2 on 2022-10-28 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_lifestyle', '0005_alter_product_home_model_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Womens_Product_Home_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Image', models.ImageField(upload_to='image/')),
                ('Category_Name', models.CharField(max_length=30)),
                ('Price', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='Product_Home_model',
            new_name='Mens_Product_Home_Model',
        ),
    ]
