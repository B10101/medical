# Generated by Django 4.1.1 on 2022-09-11 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("useracc", "0005_alter_reservation_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="status",
            field=models.CharField(
                choices=[("pending", "Pending"), ("checked", "Checked")],
                default="Pending",
                max_length=200,
                null=True,
            ),
        ),
    ]
