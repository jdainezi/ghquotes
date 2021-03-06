# Generated by Django 2.0.13 on 2019-03-27 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bitcoin', models.DecimalField(decimal_places=2, max_digits=8)),
                ('dolar', models.DecimalField(decimal_places=2, max_digits=4)),
                ('euro', models.DecimalField(decimal_places=2, max_digits=4)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
