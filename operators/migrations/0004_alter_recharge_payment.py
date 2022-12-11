# Generated by Django 4.1.4 on 2022-12-11 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
        ('operators', '0003_alter_recharge_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recharge',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recharge', to='payment.payment'),
        ),
    ]