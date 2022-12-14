# Generated by Django 4.1.4 on 2022-12-11 06:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operators', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('mode', models.CharField(choices=[('UPI', 'UPI'), ('Card', 'Card'), ('Net Banking', 'Net Banking'), ('Wallet', 'Wallet')], default='UPI', max_length=50)),
                ('tranisition_id', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operators.serviceprovider')),
            ],
        ),
    ]
