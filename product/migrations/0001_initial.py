# Generated by Django 5.2 on 2025-04-03 12:30

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
                ('name', models.CharField(max_length=20)),
                ('descriptions', models.TextField()),
                ('price', models.IntegerField()),
                ('company', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Product',
            },
        ),
    ]
