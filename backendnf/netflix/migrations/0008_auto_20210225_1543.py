# Generated by Django 3.1.4 on 2021-02-25 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0007_auto_20210225_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nfmovie',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
