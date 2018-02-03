# Generated by Django 2.0.1 on 2018-02-02 12:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0006_remove_address_public_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='secret_key',
            field=models.CharField(default=django.utils.timezone.now, max_length=64, unique=True),
            preserve_default=False,
        ),
    ]
