# Generated by Django 3.2.9 on 2021-12-02 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Project', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='financial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('Date', models.DateField(auto_now=True)),
                ('Description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('type', models.IntegerField(choices=[(1, 'deposit'), (2, 'harvest Money')])),
                ('money', models.IntegerField()),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.project')),
                ('userMoneydepositor', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('userRecipientofmoney', models.ManyToManyField(related_name='userMoneydepositor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
