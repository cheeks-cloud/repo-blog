# Generated by Django 4.0.5 on 2022-06-13 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
