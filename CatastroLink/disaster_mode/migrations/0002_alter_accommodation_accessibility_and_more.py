# Generated by Django 4.2.20 on 2025-03-30 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disaster_mode', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodation',
            name='accessibility',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='people',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='accommodation',
            name='pets',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
