# Generated by Django 4.0.4 on 2022-08-02 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_turnos', '0006_alter_tramites_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tramites',
            name='activo',
            field=models.CharField(max_length=1),
        ),
    ]
