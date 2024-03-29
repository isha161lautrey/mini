# Generated by Django 2.2.6 on 2019-10-28 15:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20191027_0427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_name', models.CharField(max_length=200)),
                ('section', models.IntegerField(choices=[(0, 'CSE-IS'), (1, 'CSE-NS'), (2, 'CSE-CORE'), (3, 'IT')], default=0)),
                ('year', models.IntegerField(choices=[(0, 'First Year'), (1, 'Second Year'), (2, 'Third Year'), (3, 'Fourth Year')], default=0)),
                ('staff', models.ForeignKey(on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
