# Generated by Django 5.0.3 on 2024-04-07 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_md5hash_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.CharField(default='', max_length=2048),
        ),
    ]
