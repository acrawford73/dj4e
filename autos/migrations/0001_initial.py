# Generated by Django 4.2 on 2024-01-18 05:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Make",
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
                    "name",
                    models.CharField(
                        help_text="Enter a make (e.g. Honda)",
                        max_length=100,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                2, "Make must be greater than 1 character"
                            )
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Autos",
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
                    "nickname",
                    models.CharField(
                        default="",
                        max_length=50,
                        validators=[
                            django.core.validators.MinLengthValidator(
                                2, "Nickname must be greater than 1 character"
                            )
                        ],
                    ),
                ),
                (
                    "mileage",
                    models.PositiveIntegerField(blank=True, default=0, null=True),
                ),
                (
                    "comments",
                    models.CharField(blank=True, default="", max_length=300, null=True),
                ),
                (
                    "make",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="autos.make"
                    ),
                ),
            ],
        ),
    ]
