# Generated by Django 4.1.1 on 2022-10-23 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("useracc", "0010_alter_customer_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="user",
            field=models.OneToOneField(
                max_length=200,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="name",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
