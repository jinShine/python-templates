# Generated by Django 3.0.4 on 2020-03-19 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='사용자명')),
                ('password', models.CharField(max_length=8, verbose_name='비밀번호')),
                ('age', models.CharField(max_length=3, null=True, verbose_name='나이')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'verbose_name': '사용자',
                'db_table': 'signup_user',
            },
        ),
    ]
