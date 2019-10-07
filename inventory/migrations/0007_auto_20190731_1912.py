# Generated by Django 2.2.3 on 2019-07-31 19:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20190731_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomeinvoice',
            name='issued_date',
            field=models.DateField(default=datetime.datetime(2019, 7, 31, 19, 12, 45, 336564, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='incomewarrant',
            name='issued_date',
            field=models.DateField(default=datetime.datetime(2019, 7, 31, 19, 12, 45, 334738, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='outcomeinvoice',
            name='issued_date',
            field=models.DateField(default=datetime.datetime(2019, 7, 31, 19, 12, 45, 337319, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='outcomewarrant',
            name='issued_date',
            field=models.DateField(default=datetime.datetime(2019, 7, 31, 19, 12, 45, 335737, tzinfo=utc)),
        ),
    ]