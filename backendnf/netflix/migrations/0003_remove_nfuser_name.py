# Generated by Django 3.1.4 on 2021-02-15 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0002_nfuser_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nfuser',
            name='name',
        ),
    ]
