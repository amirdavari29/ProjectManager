# Generated by Django 3.2.9 on 2021-12-11 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0004_auto_20211209_1218'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExpertUser',
        ),
        migrations.AddField(
            model_name='task',
            name='Estimated_end',
            field=models.DateField(blank=True, null=True),
        ),
    ]
