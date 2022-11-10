# Generated by Django 4.1.1 on 2022-10-23 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("useracc", "0012_alter_customer_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vaccine",
            name="customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]