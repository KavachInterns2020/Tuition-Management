# Generated by Django 3.0.8 on 2020-07-29 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='staff_date_joined',
            field=models.DateTimeField(null=True),
        ),
    ]