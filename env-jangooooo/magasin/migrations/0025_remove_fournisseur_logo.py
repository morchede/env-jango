# Generated by Django 4.1.7 on 2023-04-01 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("magasin", "0024_rename_img_fournisseur_logo"),
    ]

    operations = [
        migrations.RemoveField(model_name="fournisseur", name="logo",),
    ]