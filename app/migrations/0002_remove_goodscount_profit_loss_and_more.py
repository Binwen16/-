# Generated by Django 4.1 on 2022-09-05 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodscount',
            name='Profit_loss',
        ),
        migrations.RemoveField(
            model_name='goodscount',
            name='actual_goods',
        ),
        migrations.RemoveField(
            model_name='goodscount',
            name='book_goods',
        ),
        migrations.RemoveField(
            model_name='goodscount',
            name='goods',
        ),
        migrations.RemoveField(
            model_name='goodscount',
            name='remark',
        ),
        migrations.AlterField(
            model_name='receipt',
            name='drawer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sales3_orders', to='app.user', verbose_name='下单人'),
        ),
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.CharField(choices=[('sale', '销售'), ('cashier', '出纳'), ('goodsmanager', '库管')], max_length=32, verbose_name='角色'),
        ),
        migrations.CreateModel(
            name='GoodsCountDetials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_goods', models.FloatField(max_length=32, verbose_name='账面数量')),
                ('actual_goods', models.FloatField(max_length=32, verbose_name='实有数量')),
                ('Profit_loss', models.FloatField(max_length=32, verbose_name='盈亏')),
                ('remark', models.CharField(blank=True, max_length=256, null=True, verbose_name='盈亏说明')),
                ('good_count', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='good_count_set', to='app.goodscount', verbose_name='货物盘点明细')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='goods_count', to='app.goods', verbose_name='产品')),
            ],
        ),
    ]