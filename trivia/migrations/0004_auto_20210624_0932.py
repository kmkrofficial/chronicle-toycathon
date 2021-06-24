# Generated by Django 3.2.4 on 2021-06-24 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0003_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.IntegerField(default=0, null=True),
        ),
    ]