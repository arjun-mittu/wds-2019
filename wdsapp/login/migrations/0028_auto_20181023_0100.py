# Generated by Django 2.1 on 2018-10-22 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0027_auto_20181023_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstockdisplay',
            name='StockName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Stock'),
        ),
    ]