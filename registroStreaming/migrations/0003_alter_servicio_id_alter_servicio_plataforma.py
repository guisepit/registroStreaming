# Generated by Django 4.1.7 on 2023-03-30 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registroStreaming', '0002_servicio_plataforma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='plataforma',
            field=models.CharField(max_length=100, null=True),
        ),
    ]