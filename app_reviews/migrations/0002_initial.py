# Generated by Django 5.0.2 on 2024-03-20 08:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_reviews', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='review',
            index=models.Index(fields=['id'], name='app_reviews_id_5505fd_idx'),
        ),
        migrations.AddIndex(
            model_name='review',
            index=models.Index(fields=['user'], name='app_reviews_user_id_cb382e_idx'),
        ),
    ]
