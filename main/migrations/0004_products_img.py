# Generated by Django 4.1.5 on 2023-01-26 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_products_options_alter_products_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='img',
            field=models.ImageField(default='', upload_to='products_img', verbose_name='Фото'),
        ),
    ]
