# Generated by Django 4.1.2 on 2022-10-27 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carwash', '0013_freecode_alter_carwash_used_codes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='freecode',
            name='name',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
