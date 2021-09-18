# Generated by Django 3.2.7 on 2021-09-17 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pulses', '0005_rename_concusion_time_pulse_conclusion_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='pulse',
            name='player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
