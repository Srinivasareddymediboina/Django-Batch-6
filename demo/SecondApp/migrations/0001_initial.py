# Generated by Django 3.0.7 on 2020-09-22 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
