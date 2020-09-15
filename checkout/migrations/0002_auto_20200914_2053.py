# Generated by Django 3.1.1 on 2020-09-14 20:53

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200910_1629'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='product_size',
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='occasion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.occasion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='package',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.package'),
            preserve_default=False,
        ),
    ]