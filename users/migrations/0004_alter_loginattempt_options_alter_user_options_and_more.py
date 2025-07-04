# Generated by Django 5.0.7 on 2025-02-08 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_loginattempt_options_alter_loginattempt_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loginattempt',
            options={'verbose_name': 'Спроба входу', 'verbose_name_plural': 'Спроби входу'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Користувач', 'verbose_name_plural': 'Користувачі'},
        ),
        migrations.AlterModelOptions(
            name='usersgroup',
            options={'verbose_name': 'Група', 'verbose_name_plural': 'Групи'},
        ),
        migrations.AlterModelOptions(
            name='usersgroupmembership',
            options={'verbose_name': 'Членство користувача в групі', 'verbose_name_plural': 'Членство користувача в групах'},
        ),
        migrations.AlterField(
            model_name='usersgroupmembership',
            name='owner',
            field=models.BooleanField(default=False, verbose_name='Вчитель групи'),
        ),
    ]
