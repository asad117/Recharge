# Generated by Django 4.1.4 on 2022-12-11 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
        ('operators', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recharge',
            name='payment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recharge', to='payment.payment'),
        ),
    ]
