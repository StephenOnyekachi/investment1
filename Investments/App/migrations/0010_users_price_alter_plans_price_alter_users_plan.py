# Generated by Django 4.2.1 on 2023-08-30 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_users_parcent_alter_users_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='plans',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='users',
            name='plan',
            field=models.TextField(null=True),
        ),
    ]
