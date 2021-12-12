    # Generated by Django 3.2.9 on 2021-12-09 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Step', '0001_initial'),
        ('Task', '0003_task_expert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='StepID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Step.step'),
        ),
        migrations.AlterField(
            model_name='task',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='startDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'deActive'), (1, 'Active'), (2, 'Faile')], default=0, null=True),
        ),
    ]
