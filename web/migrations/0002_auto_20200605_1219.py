# Generated by Django 3.0.6 on 2020-06-05 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='anount',
            new_name='amount',
        ),
    ]