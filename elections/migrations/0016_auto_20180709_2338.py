# Generated by Django 2.0.7 on 2018-07-10 03:38

from django.db import migrations, models


def combine_precinct_number_and_letter(apps, schema_editor):
    Poll = apps.get_model('elections', 'Poll')
    for poll in Poll.objects.all():

        if poll.ward_number:
            poll.ward = str(poll.ward_number).strip()
        else:
            poll.ward = ''

        if poll.precinct_number:
            poll.precinct = (
                f'{poll.precinct_number}{poll.precinct_letter}'.strip()
            )
        else:
            poll.precinct = ''

        poll.save()


class Migration(migrations.Migration):

    dependencies = [('elections', '0015_registrationstatus_poll')]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='precinct',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AddField(
            model_name='poll',
            name='ward',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.RunPython(combine_precinct_number_and_letter),
    ]
