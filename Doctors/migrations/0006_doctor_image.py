# Generated by Django 2.2.5 on 2019-09-15 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0005_doctor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]