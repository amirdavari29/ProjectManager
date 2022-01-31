# Generated by Django 3.2.10 on 2022-01-26 16:31

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
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('Date', models.DateField(auto_now=True, verbose_name='تاریخ واریز')),
                ('Description', models.TextField(verbose_name='توضیحات')),
                ('image', models.ImageField(null=True, upload_to='financial/images', verbose_name='عکس واریزی ')),
                ('type', models.IntegerField(choices=[(1, 'واریز '), (2, ' برداشت')], verbose_name='نوع')),
                ('money', models.CharField(max_length=50, verbose_name='مقدار پول')),
                ('creator_financial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='creator_financial', to=settings.AUTH_USER_MODEL)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.project', verbose_name='نام  پروژه')),
                ('userMoneydepositor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='پرداخت کننده')),
                ('userRecipientofmoney', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userMoneydepositor', to=settings.AUTH_USER_MODEL, verbose_name='دریافت کننده')),
            ],
            options={
                'verbose_name': 'مالی',
                'verbose_name_plural': 'لیست مالی',
            },
        ),
    ]
