# Generated by Django 3.0.2 on 2020-02-02 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_distributer_catalog'),
    ]

    operations = [
        migrations.AddField(
            model_name='distributer_catalog',
            name='catalog_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]