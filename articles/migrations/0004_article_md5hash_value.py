# Generated by Django 5.0.3 on 2024-04-06 21:04

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='md5hash_value',
            field=models.CharField(default=articles.models.return_rand, max_length=35),
        ),
    ]