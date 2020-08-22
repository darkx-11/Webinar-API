# Generated by Django 3.0.8 on 2020-07-24 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webinars', '0002_delete_webinarsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='webinarsmodel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('task_heading', models.CharField(max_length=100)),
                ('task_details', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]