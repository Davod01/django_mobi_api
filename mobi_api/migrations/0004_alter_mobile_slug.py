# Generated by Django 4.2.2 on 2023-06-30 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobi_api', '0003_alter_mobile_display_size_alter_mobile_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=200, unique=True),
        ),
    ]