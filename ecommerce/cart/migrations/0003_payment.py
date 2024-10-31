# Generated by Django 5.1.2 on 2024-10-22 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_order_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('amount', models.IntegerField()),
                ('order_id', models.CharField(blank=True, max_length=30)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=20)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]
