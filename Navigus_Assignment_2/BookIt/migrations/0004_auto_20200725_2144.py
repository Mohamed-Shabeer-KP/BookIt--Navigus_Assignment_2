# Generated by Django 3.0.8 on 2020-07-25 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookIt', '0003_slot_host'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='attendee',
            field=models.CharField(help_text='attendee username', max_length=30, null=True),
        ),
    ]
