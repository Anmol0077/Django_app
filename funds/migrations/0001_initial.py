# Generated by Django 4.0.7 on 2022-10-02 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompaniesName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cp_id', models.CharField(max_length=60)),
                ('cp_name', models.CharField(max_length=60)),
                ('mf_id', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('alias', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='MutualFunds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mf_id', models.CharField(max_length=60)),
                ('mf_name', models.CharField(max_length=60)),
            ],
        ),
    ]
