# Generated by Django 4.2.3 on 2023-08-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_alter_personne_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='points',
            field=models.IntegerField(),
        ),
    ]
