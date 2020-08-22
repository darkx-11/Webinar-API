# Generated by Django 3.0.8 on 2020-08-20 20:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webinars', '0006_auto_20200802_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='webinarsmodel',
            name='webinar_registration',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='webinarsmodel',
            name='webinar_image',
            field=models.ImageField(upload_to=''),
        ),
    ]