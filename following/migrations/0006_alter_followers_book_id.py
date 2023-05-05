# Generated by Django 4.2 on 2023-05-04 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0003_alter_book_users_following"),
        ("following", "0005_rename_follower_id_followers_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="followers",
            name="book_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="book_following",
                to="books.book",
                unique=True,
            ),
        ),
    ]
