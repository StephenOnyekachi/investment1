# Generated by Django 4.2.1 on 2023-08-31 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_remove_histories_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='picture',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
    ]
