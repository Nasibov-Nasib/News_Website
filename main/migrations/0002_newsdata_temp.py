# Generated by Django 4.0.6 on 2022-12-06 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsdata',
            name='temp',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
