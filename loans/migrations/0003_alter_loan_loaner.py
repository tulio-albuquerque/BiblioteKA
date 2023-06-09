# Generated by Django 4.2 on 2023-05-03 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("loans", "0002_loan_copy_loan_loaner_loan_return_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loan",
            name="loaner",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_copy_loan",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
