# Generated by Django 4.0.2 on 2022-02-23 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_category_options_alter_tags_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='birnimadir-nimadie'),
            preserve_default=False,
        ),
    ]
