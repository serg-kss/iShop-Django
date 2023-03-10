# Generated by Django 4.1.5 on 2023-02-20 13:55

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_orders_goods'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='options',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='S', max_length=1, verbose_name='Опции'),
        ),
        migrations.AlterField(
            model_name='products',
            name='supplier',
            field=models.ForeignKey(default=main.models.Supplier, on_delete=django.db.models.deletion.CASCADE, to='main.supplier', verbose_name='Поставщик'),
        ),
    ]
