# Generated by Django 4.1.5 on 2023-01-06 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adverseemail',
            name='candidate',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.candidate'),
        ),
    ]
