# Generated by Django 3.1.5 on 2021-01-05 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='roll_no',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]