# Generated by Django 4.1.3 on 2022-11-27 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SholatDoa",
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
                ("judul", models.CharField(max_length=200)),
                ("deskripsi", models.TextField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("idcol", models.CharField(max_length=200)),
                (
                    "nama",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Bacaan Sholat",
            },
        ),
        migrations.CreateModel(
            name="DoaDoa",
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
                ("judul", models.CharField(max_length=200)),
                ("deskripsi", models.TextField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("idcol", models.CharField(max_length=200)),
                (
                    "nama",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Doa",
            },
        ),
    ]
