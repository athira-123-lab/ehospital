# Generated by Django 4.2.16 on 2024-09-25 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehosp_app', '0003_appointment_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='amount',
        ),
    ]
