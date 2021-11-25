# Generated by Django 2.2.10 on 2021-11-24 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('start_date', models.DateField(verbose_name='start_date')),
                ('stop_date', models.DateField(verbose_name='stop_date')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(verbose_name='text_of_question')),
                ('question_type', models.CharField(choices=[('text', 'text_only'), ('sc', 'single_choice'), ('mc', 'multiple_choices')], default='text', max_length=20, verbose_name='type_of_question')),
                ('questionnaire_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Questionnaire')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField(verbose_name='answer_text')),
                ('user_id', models.IntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Question')),
            ],
        ),
    ]