# Generated by Django 4.1.2 on 2022-10-27 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carwash', '0014_freecode_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freecode',
            name='name',
            field=models.CharField(default='name', max_length=50),
        ),
    ]
