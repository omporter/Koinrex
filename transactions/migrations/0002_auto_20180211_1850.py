# Generated by Django 2.0.1 on 2018-02-11 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deposits',
            options={'verbose_name': 'Deposit', 'verbose_name_plural': 'Deposits'},
        ),
        migrations.AlterModelOptions(
            name='withdrawals',
            options={'verbose_name': 'Withdrawal', 'verbose_name_plural': 'Withdrawals'},
        ),
    ]
