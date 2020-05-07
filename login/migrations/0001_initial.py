# Generated by Django 2.2.6 on 2019-10-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=100)),
                ('e_mail', models.EmailField(max_length=254, unique=True)),
                ('c_time', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'ordering': ['c_time'],
            },
        ),
    ]
