# Generated by Django 3.1 on 2022-06-02 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_question_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='unit',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]