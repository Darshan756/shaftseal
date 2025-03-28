# Generated by Django 5.1.7 on 2025-03-21 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Spares", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ModelPart",
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
                (
                    "model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="common_parts",
                        to="Spares.pumpmodel",
                    ),
                ),
                (
                    "part",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Spares.part"
                    ),
                ),
            ],
        ),
    ]
