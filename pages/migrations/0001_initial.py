# Generated by Django 3.1.13 on 2021-11-20 19:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_code', models.CharField(max_length=60)),
                ('title', models.CharField(max_length=400)),
                ('display', models.BooleanField(default=True)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField(default='', editable=False, max_length=60)),
            ],
            options={
                'ordering': ['date_added'],
            },
        ),
    ]