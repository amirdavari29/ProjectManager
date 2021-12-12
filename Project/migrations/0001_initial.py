# Generated by Django 3.2.9 on 2021-12-02 09:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('status', models.IntegerField(choices=[(1, 'Done'), (2, 'deActive'), (3, 'Active'), (4, 'Fail')], default=2)),
                ('Experts', models.ManyToManyField(related_name='creator_set', to=settings.AUTH_USER_MODEL)),
                ('ScrumMaster', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
