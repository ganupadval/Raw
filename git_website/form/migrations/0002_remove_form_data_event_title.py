# Generated by Django 4.0.3 on 2022-07-27 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form_data',
            name='event_title',
        ),
    ]