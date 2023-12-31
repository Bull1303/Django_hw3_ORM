# Generated by Django 4.2.3 on 2023-08-22 13:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Phone",
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
                ("name", models.CharField(max_length=50)),
                ("price", models.IntegerField()),
                ("image", models.FileField(upload_to="")),
                ("release_date", models.DateField()),
                ("lte_exists", models.BooleanField(default=False)),
                ("slug", models.SlugField(unique=True)),
            ],
        ),
    ]
