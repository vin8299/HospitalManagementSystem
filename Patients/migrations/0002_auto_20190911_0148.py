# Generated by Django 2.2.5 on 2019-09-10 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='ward_no',
            field=models.CharField(max_length=50),
        ),
    ]
