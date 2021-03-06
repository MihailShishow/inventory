# Generated by Django 2.2.3 on 2019-08-09 17:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20190806_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomeinvoice',
            name='issued_date',
            field=models.DateField(default=datetime.datetime(2019, 8, 9, 17, 55, 23, 77606, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='incomewarrant',
            name='issued_date',
            field=models.DateField(default=datetime.datetime(2019, 8, 9, 17, 55, 23, 75956, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='outcomeinvoice',
            name='issued_date',
            field=models.DateField(default=datetime.datetime(2019, 8, 9, 17, 55, 23, 78367, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='outcomewarrant',
            name='issued_date',
            field=models.DateField(default=datetime.datetime(2019, 8, 9, 17, 55, 23, 76799, tzinfo=utc)),
        ),
    ]
