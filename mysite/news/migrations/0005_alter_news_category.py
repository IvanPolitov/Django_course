# Generated by Django 5.0.6 on 2024-07-16 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='news.category', verbose_name='Категория'),
            preserve_default=False,
        ),
    ]
