# Generated by Django 3.2.10 on 2022-01-29 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Task', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام ')),
                ('type_id', models.IntegerField(choices=[(0, 'image'), (1, 'pdf'), (2, 'doc'), (3, 'zip')], verbose_name='نوع')),
                ('path', models.FileField(blank=True, null=True, upload_to='Attach/file', verbose_name='آدرس ')),
                ('status', models.IntegerField(choices=[(1, 'disable'), (2, 'done')], verbose_name='وضعیت')),
                ('doneDate', models.DateField(auto_now_add=True, null=True, verbose_name='تاریخ انجام ')),
                ('createDate', models.DateField(auto_now=True, verbose_name='تاریخ ایجاد  ')),
                ('creator_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='نام ایجاد کننده')),
            ],
            options={
                'verbose_name': 'ضمیمه',
                'verbose_name_plural': 'فایلهای ضمیمه',
            },
        ),
        migrations.CreateModel(
            name='Validation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان ')),
                ('description', models.TextField(max_length=5000, verbose_name='توضیحات')),
                ('status', models.IntegerField(choices=[(1, 'disable'), (2, 'done')], verbose_name='وضعیت')),
                ('doneDate', models.DateField(auto_now=True, verbose_name='تاریخ انجام ')),
                ('createDate', models.DateField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد  ')),
                ('creator_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='نام ایجاد کننده')),
                ('task_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Task.task', verbose_name='نام تسک')),
            ],
            options={
                'verbose_name': ' اعتبار سنحی',
                'verbose_name_plural': 'اعتبار سنجی ها',
            },
        ),
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان ')),
                ('status', models.IntegerField(choices=[(1, 'disable'), (2, 'done')], verbose_name='وضعیت')),
                ('doneDate', models.DateField(auto_now=True, verbose_name='تاریخ انجام ')),
                ('createDate', models.DateField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد  ')),
                ('creator_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='نام ایجاد کننده')),
                ('task_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Task.task', verbose_name='نام تسک')),
            ],
            options={
                'verbose_name': 'تست',
                'verbose_name_plural': 'تست ها ',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان ')),
                ('code', models.TextField(max_length=5000, verbose_name='کد')),
                ('status', models.IntegerField(choices=[(1, 'disable'), (2, 'done')], verbose_name='وضعیت')),
                ('doneDate', models.DateField(auto_now=True, verbose_name='تاریخ انجام ')),
                ('createDate', models.DateField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد  ')),
                ('creator_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='نام ایجاد کننده')),
                ('task_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Task.task', verbose_name='نام تسک')),
            ],
            options={
                'verbose_name': 'پیغام',
                'verbose_name_plural': 'پیغام ها',
            },
        ),
        migrations.CreateModel(
            name='Develop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
                ('method', models.IntegerField(choices=[(1, 'get'), (2, 'put'), (3, 'post'), (4, 'delete')], verbose_name=' متد')),
                ('url', models.CharField(max_length=200, verbose_name='آدرس ')),
                ('param', models.CharField(blank=True, max_length=200, null=True, verbose_name='پارامتر')),
                ('response', models.TextField(blank=True, max_length=200, null=True, verbose_name='بازخورد')),
                ('doneDate', models.DateField(auto_now=True, verbose_name='تاریخ انجام شدن')),
                ('createDate', models.DateField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('attach_ids', models.ManyToManyField(to='Api.Attach', verbose_name='ضمیمه')),
                ('creator_uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='UserCreator', to=settings.AUTH_USER_MODEL, verbose_name='نام ایجاد کننده')),
                ('task_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Task.task', verbose_name='نام تسک')),
            ],
            options={
                'verbose_name': 'توسعه ',
                'verbose_name_plural': 'توسعه ها ',
            },
        ),
    ]
