# Generated by Django 4.0.4 on 2022-08-04 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_turnos', '0010_alter_clientes_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='picture',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
