# Generated by Django 4.1.1 on 2022-10-23 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("useracc", "0008_reservation_customer"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
            ],
        ),
    ]