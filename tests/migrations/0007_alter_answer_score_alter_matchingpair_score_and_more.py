# Generated by Django 5.0.7 on 2025-05-29 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0006_answer_score_matchingpair_score_question_scores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='score',
            field=models.IntegerField(default=1, verbose_name='Бали за відповідь'),
        ),
        migrations.AlterField(
            model_name='matchingpair',
            name='score',
            field=models.IntegerField(default=1, verbose_name='Бали за відповідність'),
        ),
        migrations.AlterField(
            model_name='question',
            name='scores',
            field=models.IntegerField(default=1, verbose_name='Бали за питання'),
        ),
    ]
