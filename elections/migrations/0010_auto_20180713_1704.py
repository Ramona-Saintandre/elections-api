# Generated by Django 2.0.7 on 2018-07-13 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('elections', '0009_ballotwebsite_source')]

    operations = [
        migrations.AddField(
            model_name='ballotwebsite',
            name='fetched',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='precinct',
            unique_together={('county', 'jurisdiction', 'ward', 'precinct')},
        ),
    ]