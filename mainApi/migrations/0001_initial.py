# Generated by Django 2.2.3 on 2019-07-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(max_length=11)),
                ('branch_id', models.BigIntegerField()),
                ('branch', models.CharField(max_length=74)),
                ('address', models.CharField(max_length=195)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=26)),
                ('bank_name', models.CharField(max_length=49)),
            ],
        ),
    ]
