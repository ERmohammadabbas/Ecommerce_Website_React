# Generated by Django 3.2.4 on 2021-06-18 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_stripemodel_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripemodel',
            name='customer_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
