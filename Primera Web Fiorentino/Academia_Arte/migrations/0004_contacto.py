# Generated by Django 4.0.3 on 2022-07-04 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academia_Arte', '0003_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_contacto', models.CharField(max_length=20)),
                ('email_contacto', models.EmailField(max_length=254)),
                ('tel_contacto', models.IntegerField()),
                ('asunto_contacto', models.CharField(max_length=40)),
                ('mensaje_contacto', models.CharField(max_length=500)),
            ],
        ),
    ]
