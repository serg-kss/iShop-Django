# Generated by Django 4.1.5 on 2023-02-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_orders_email_alter_orders_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='goods',
            field=models.CharField(default='', max_length=250, verbose_name='Товары'),
        ),
    ]
