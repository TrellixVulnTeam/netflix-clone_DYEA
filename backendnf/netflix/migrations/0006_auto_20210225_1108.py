# Generated by Django 3.1.4 on 2021-02-25 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netflix', '0005_nfuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nfmovie',
            name='category_id',
            field=models.SmallIntegerField(),
        ),
    ]
