# Generated by Django 4.2.1 on 2023-06-01 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_port_reason_remove_port_rpc_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='port',
            name='reason',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
