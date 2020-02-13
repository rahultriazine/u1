# Generated by Django 3.0.2 on 2020-02-03 10:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_auto_20200203_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale_to_customers',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 3, 10, 22, 28, 355608, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='sale_to_customers',
            name='date_modified',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 3, 10, 22, 28, 355644, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='sale_to_customers',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sale_to_customers',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sale_to_customers_detail',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 3, 10, 22, 28, 356198, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='sale_to_customers_detail',
            name='date_modified',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 3, 10, 22, 28, 356221, tzinfo=utc), null=True),
        ),
    ]