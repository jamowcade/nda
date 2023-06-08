# Generated by Django 4.2.1 on 2023-06-07 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_port_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLoggers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('device', models.TextField(null=True)),
                ('logger_name', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]