# Generated by Django 5.1.3 on 2025-02-09 04:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=41)),
                ('birth_date', models.DateField()),
                ('last_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SkillMaster',
            fields=[
                ('skill_id', models.AutoField(primary_key=True, serialize=False)),
                ('skill_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingMaster',
            fields=[
                ('training_id', models.AutoField(primary_key=True, serialize=False)),
                ('training_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.skillmaster')),
            ],
            options={
                'unique_together': {('employee', 'skill')},
            },
        ),
        migrations.CreateModel(
            name='EmployeeTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.trainingmaster')),
            ],
            options={
                'unique_together': {('employee', 'training')},
            },
        ),
    ]
