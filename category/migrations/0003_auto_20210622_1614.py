# Generated by Django 3.1 on 2021-06-22 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20210622_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, max_length=255, verbose_name='descripcion'),
        ),
    ]