# Generated by Django 3.2.3 on 2021-05-31 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_userfeedback_review_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfeedback',
            name='review_date',
        ),
    ]