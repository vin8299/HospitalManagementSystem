# Generated by Django 2.2.5 on 2019-09-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0003_remove_doctor_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='contact_no',
            field=models.CharField(default=0, max_length=15),
        ),
    ]
