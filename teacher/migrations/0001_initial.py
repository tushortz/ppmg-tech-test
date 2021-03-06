# Generated by Django 3.1.7 on 2021-04-06 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone_no', models.CharField(max_length=50)),
                ('room_no', models.CharField(max_length=10)),
                ('profile_pic', models.TextField(max_length=300)),
                ('subjects_taught', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
            },
        ),
    ]
