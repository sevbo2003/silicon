# Generated by Django 4.0.2 on 2022-02-24 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_subscriber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='default_avatar.png', upload_to='avatars'),
        ),
    ]
