# Generated by Django 5.0.1 on 2024-02-03 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0002_alter_trainee_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainee',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='trainee/media'),
        ),
    ]