# Generated by Django 2.2.3 on 2019-07-31 18:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20190731_1849'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outcomeinvoice',
            old_name='gicen_to',
            new_name='given_to',
        ),
        migrations.RenameField(
            model_name='outcomewarrant',
            old_name='received_from',
            new_name='given_to',
        ),
        migrations.AlterField(
            model_name='incomeinvoice',
            name='issued_date',
            field=models.DateField(default=datetime.datetime(2019, 7, 31, 18, 54, 5, 116340, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='incomeinvoice',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='incomewarrant',
            name='issued_date',
            field=models.DateField(default=datetime.datetime(2019, 7, 31, 18, 54, 5, 114866, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='outcomeinvoice',
            name='issued_date',
            field=models.DateField(default=datetime.datetime(2019, 7, 31, 18, 54, 5, 117075, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='outcomeinvoice',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='outcomewarrant',
            name='cash_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='outcomewarrant',
            name='issued_date',
            field=models.DateField(default=datetime.datetime(2019, 7, 31, 18, 54, 5, 115620, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productincome',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='productincome',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='productincome',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='productoutcome',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='productoutcome',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='productoutcome',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
