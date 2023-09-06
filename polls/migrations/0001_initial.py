# Generated by Django 4.2.5 on 2023-09-06 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_name', models.CharField(default='', max_length=25)),
                ('market_type', models.CharField(default='', max_length=25)),
            ],
            options={
                'db_table': 'polls_market',
            },
        ),
        migrations.CreateModel(
            name='Supermarket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smarket_name', models.CharField(default='', max_length=25)),
                ('smarket_type', models.CharField(default='', max_length=25)),
            ],
        ),
    ]