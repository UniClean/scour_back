# Generated by Django 4.1.7 on 2023-03-04 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='accept_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='completed_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='supervisor_comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
