# Generated by Django 4.1.2 on 2022-10-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carwash', '0015_alter_freecode_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freecode',
            name='name',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
