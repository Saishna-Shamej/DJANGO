# Generated by Django 5.0.1 on 2024-02-08 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=24)),
                ('item_img', models.ImageField(upload_to='')),
            ],
        ),
    ]
