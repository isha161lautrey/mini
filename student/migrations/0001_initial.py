# Generated by Django 2.2 on 2019-10-26 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=200)),
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('year', models.IntegerField(choices=[(0, 'First Year'), (1, 'Second Year'), (2, 'Third Year'), (3, 'Fourth Year')])),
                ('section', models.IntegerField(choices=[(0, 'CSE-IS'), (1, 'CSE-NS'), (2, 'CSE-CORE'), (3, 'IT')])),
                ('password', models.CharField(max_length=100)),
                ('is_admin', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=True)),
                ('is_teacher', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
