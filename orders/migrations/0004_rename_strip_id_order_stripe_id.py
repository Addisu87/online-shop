# Generated by Django 5.0.6 on 2024-06-05 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_strip_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='strip_id',
            new_name='stripe_id',
        ),
    ]
