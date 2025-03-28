# Generated by Django 5.1.7 on 2025-03-21 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Spares", "0002_modelpart"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="modelpart",
            constraint=models.UniqueConstraint(
                fields=("model", "part"), name="unique_model_part"
            ),
        ),
        migrations.AddConstraint(
            model_name="modelvariantpart",
            constraint=models.UniqueConstraint(
                fields=("variant", "part"), name="unique_variant_part"
            ),
        ),
    ]
