# Generated by Django 4.2.6 on 2023-10-14 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventoAdmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='hora',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='nombre_persona',
            field=models.CharField(default='Anonimo', max_length=200),
        ),
    ]