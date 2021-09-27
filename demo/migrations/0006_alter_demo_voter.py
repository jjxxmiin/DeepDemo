# Generated by Django 3.2.7 on 2021-09-27 14:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('demo', '0005_demo_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo',
            name='voter',
            field=models.ManyToManyField(related_name='voter_demo', to=settings.AUTH_USER_MODEL),
        ),
    ]
