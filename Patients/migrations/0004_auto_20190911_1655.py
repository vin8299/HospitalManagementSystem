# Generated by Django 2.2.5 on 2019-09-11 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patients', '0003_patient_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='p_age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patient',
            name='p_sex',
            field=models.CharField(default=None, max_length=10),
        ),
    ]