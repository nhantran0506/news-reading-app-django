# Generated by Django 4.1.13 on 2024-05-29 10:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0003_alter_article_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="image",
            field=models.TextField(blank=True, null=True),
        ),
    ]