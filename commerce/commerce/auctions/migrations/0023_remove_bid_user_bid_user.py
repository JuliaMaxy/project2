# Generated by Django 4.2.1 on 2023-06-09 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_remove_bid_user_bid_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='user',
        ),
        migrations.AddField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bids', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
