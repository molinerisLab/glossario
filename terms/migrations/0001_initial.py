# Generated by Django 5.0 on 2023-12-29 13:36

import django.db.models.deletion
import markdownx.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Topic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Term",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, unique=True)),
                ("short_version", models.CharField(max_length=200)),
                ("long_version", markdownx.models.MarkdownxField()),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="terms.subject"
                    ),
                ),
                (
                    "topic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="terms.topic"
                    ),
                ),
            ],
        ),
    ]
