# Generated by Django 4.0.3 on 2023-03-27 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_results_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='rank',
            field=models.IntegerField(default=0, verbose_name='id'),
        ),
    ]
