# Generated by Django 3.2.4 on 2021-06-22 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
