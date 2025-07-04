# Generated by Django 5.0.7 on 2025-06-22 07:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0011_alter_question_scores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='score',
            field=models.FloatField(default=0, verbose_name='Бали за відповідь'),
        ),
        migrations.AlterField(
            model_name='matchingpair',
            name='score',
            field=models.FloatField(default=1, verbose_name='Бали за відповідність'),
        ),
        migrations.AlterField(
            model_name='question',
            name='scores',
            field=models.FloatField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(500.0)], verbose_name='Бали за питання'),
        ),
    ]
