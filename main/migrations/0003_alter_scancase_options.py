# Generated by Django 4.1.7 on 2023-05-14 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_userloggers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scancase',
            options={'permissions': [('can_compare_scancase', 'Can compare Scancase')]},
        ),
    ]
