# Generated by Django 2.1.5 on 2019-01-30 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RDApp', '0004_auto_20190130_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reconupdate',
            name='UpdateDate',
        ),
        migrations.RemoveField(
            model_name='reconupdate',
            name='UserId',
        ),
    ]
