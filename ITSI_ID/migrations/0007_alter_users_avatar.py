# Generated by Django 5.0.4 on 2024-04-20 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITSI_ID', '0006_alter_users_avatar_alter_users_products_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar'),
        ),
    ]