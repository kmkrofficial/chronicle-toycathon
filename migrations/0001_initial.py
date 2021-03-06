# Generated by Django 3.2.4 on 2021-06-22 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=25)),
                ('video', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('question', models.TextField(max_length=500)),
                ('answer', models.TextField(max_length=500)),
                ('choice1', models.TextField(max_length=500)),
                ('choice2', models.TextField(max_length=500)),
                ('choice3', models.TextField(max_length=500)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='trivia.category')),
            ],
        ),
    ]
