# Generated by Django 3.1.5 on 2022-07-25 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explodindoMentes', '0003_auto_20220720_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office',
            name='sector',
        ),
        migrations.RemoveField(
            model_name='sector',
            name='position',
        ),
    ]
