# Generated by Django 4.2 on 2023-05-02 18:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_is_admin_user_is_blocked_user_role_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
    ]
