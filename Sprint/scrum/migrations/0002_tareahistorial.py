# Generated by Django 5.1 on 2024-10-24 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TareaHistorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_anterior', models.CharField(max_length=20)),
                ('estado_nuevo', models.CharField(max_length=20)),
                ('fecha_cambio', models.DateTimeField(auto_now_add=True)),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrum.tarea')),
            ],
        ),
    ]