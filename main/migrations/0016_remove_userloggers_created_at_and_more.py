# Generated by Django 4.2.2 on 2023-06-07 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_rename_devive_errorlog_device'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userloggers',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='userloggers',
            name='device',
        ),
        migrations.RemoveField(
            model_name='userloggers',
            name='logger_name',
        ),
        migrations.RemoveField(
            model_name='userloggers',
            name='message',
        ),
        migrations.AddField(
            model_name='userlog',
            name='device',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='userlog',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='userlog',
            name='user',
            field=models.TextField(),
        ),
    ]