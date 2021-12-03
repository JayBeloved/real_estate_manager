# Generated by Django 3.2.8 on 2021-12-01 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accrequest',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Payment Verified'), (0, 'Verification Pending')], default=0, verbose_name='request_status'),
        ),
    ]
