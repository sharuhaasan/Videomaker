# Generated by Django 4.2.2 on 2023-07-01 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Audio_Elements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audioelement',
            name='video_component_id',
            field=models.IntegerField(null=True),
        ),
    ]
