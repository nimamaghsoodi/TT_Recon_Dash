# Generated by Django 2.1.5 on 2019-05-02 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RDApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewReconUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReconUser', models.CharField(max_length=30)),
                ('ReconTitle', models.CharField(max_length=100)),
                ('ReconTotalCount', models.IntegerField()),
                ('ReconExecutedCount', models.IntegerField()),
                ('ReconType', models.CharField(max_length=20)),
                ('ReconDateTime', models.DateTimeField()),
                ('ReconComments', models.CharField(blank=True, default=None, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReconAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DefinedUser', models.CharField(max_length=30)),
                ('UserFullName', models.CharField(max_length=50)),
                ('UserReconTitle', models.CharField(max_length=100)),
                ('UserReconType', models.CharField(max_length=15)),
                ('OccuranceNum', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='reconupdate',
            name='UpdateDate',
        ),
        migrations.AddField(
            model_name='reconupdate',
            name='ReconTime',
            field=models.TimeField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reconupdate',
            name='ReconType',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
    ]
