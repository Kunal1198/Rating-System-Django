# Generated by Django 2.0.3 on 2018-10-25 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20181026_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='current_cgpa',
            field=models.IntegerField(default=''),
        ),
    ]