# Generated by Django 5.1.3 on 2024-12-03 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('stock_quantity', models.PositiveIntegerField(default=0, verbose_name='Quantity in Stock')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]