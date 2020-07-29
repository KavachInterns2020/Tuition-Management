# Generated by Django 3.0.8 on 2020-07-29 16:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_merge_20200729_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='enrollment_name',
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_date_joined',
            field=models.DateField(default=datetime.datetime(2020, 7, 29, 16, 51, 27, 518449)),
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('enrollment_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('subject_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Subject')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='enrollment_name',
            field=models.ForeignKey(default='CSE', on_delete=django.db.models.deletion.CASCADE, to='home.Enrollment'),
        ),
    ]