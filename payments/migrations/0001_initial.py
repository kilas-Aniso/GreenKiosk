# Generated by Django 4.2.1 on 2023-06-21 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('method', models.CharField(max_length=32)),
                ('Payment_status', models.CharField(max_length=32)),
                ('Payment_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
