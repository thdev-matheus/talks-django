# Generated by Django 4.1.2 on 2022-11-07 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_alter_post_created_at_alter_post_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.URLField(blank=True, null=True),
        ),
    ]
