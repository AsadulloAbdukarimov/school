# Generated by Django 4.2.5 on 2023-12-15 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BestPupils',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pupil_name', models.CharField(max_length=30, verbose_name='Ism')),
                ('pupil_surname', models.CharField(max_length=30, verbose_name='Familyas')),
                ('pupil_achievements', models.TextField(verbose_name='Yutuqlari')),
                ('pupil_smm', models.URLField(verbose_name='Ijtimoiy tarmoqdagi sahifalari uchun link')),
            ],
            options={
                'db_table': 'best_pupils',
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255, verbose_name='Kurs nomi')),
                ('course_desc', models.CharField(max_length=200, verbose_name='Kurs haqida izoh ')),
                ('course_teacher', models.CharField(max_length=200, verbose_name="Kurs o'qituvchisi")),
                ('course_price', models.IntegerField(blank=True, null=True, verbose_name='Kurs narxi')),
            ],
            options={
                'db_table': 'courses',
            },
        ),
        migrations.CreateModel(
            name='Exam_materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.TextField(verbose_name="Imtixon uchun Ma'lumot")),
                ('links', models.URLField(blank=True, null=True, verbose_name='Material uchun link')),
                ('material_dateTime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'materials',
                'ordering': ('-material_dateTime',),
            },
        ),
    ]
