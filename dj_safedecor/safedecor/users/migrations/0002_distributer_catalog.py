# Generated by Django 3.0.2 on 2020-02-02 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distributer_Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalog_code', models.CharField(blank=True, max_length=100, null=True)),
                ('distributer_id', models.CharField(blank=True, max_length=100, null=True)),
                ('catalog_image', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Distributer Catalog',
                'verbose_name_plural': 'Distributer Catalog',
                'managed': True,
            },
        ),
    ]