# Generated by Django 4.1.7 on 2023-03-12 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_accept_time_order_completed_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='report_deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='start_when',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
