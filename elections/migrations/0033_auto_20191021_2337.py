# Generated by Django 2.2.6 on 2019-10-22 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0032_ballotwebsite_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
