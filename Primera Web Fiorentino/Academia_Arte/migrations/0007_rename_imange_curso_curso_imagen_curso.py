# Generated by Django 4.0.5 on 2022-07-08 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Academia_Arte', '0006_curso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='imange_curso',
            new_name='imagen_curso',
        ),
    ]