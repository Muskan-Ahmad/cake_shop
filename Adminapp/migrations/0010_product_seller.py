# Generated by Django 4.2 on 2023-09-03 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Adminapp", "0009_remove_userinfo_add"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="seller",
            field=models.CharField(default="bakingo Ujjain", max_length=50),
            preserve_default=False,
        ),
    ]