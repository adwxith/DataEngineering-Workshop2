# Generated by Django 5.1.1 on 2024-10-04 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_remove_students_id_students_branch_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('salary', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=10)),
                ('role', models.CharField(choices=[('HR', 'HR'), ('Devloper', 'Devloper'), ('Team_Lead', 'TeamLead'), ('Tester', 'Tester')], max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='students',
            name='roll_number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
