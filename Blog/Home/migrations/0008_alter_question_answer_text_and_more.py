# Generated by Django 4.0.5 on 2022-08-16 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_question_answer_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer_text',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='result_kanji_text',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
