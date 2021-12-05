# Generated by Django 3.2.9 on 2021-12-05 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0002_remove_doctor_time_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='booker.speciality'),
        ),
    ]
