# Generated by Django 4.1 on 2022-09-11 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_goodscount_profit_loss_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashbalance',
            name='data',
            field=models.DateField(default='2022-09-02', verbose_name='时间'),
        ),
    ]