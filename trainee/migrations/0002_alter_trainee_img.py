# Generated by Django 5.0.1 on 2024-01-31 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='img',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
