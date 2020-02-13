# Generated by Django 3.0.3 on 2020-02-12 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_of_education', models.CharField(choices=[('PHD', 'PHD'), ('Masters', 'Masters'), ('Under Graduate', 'Under Graduate'), ('Form Four Leaver', 'Form Four Leaver')], max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Manager', 'Manager'), ('IT Technician', 'IT Technician'), ('Sales Person', 'Sales Person')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('emp_code', models.CharField(max_length=30, unique=True)),
                ('mobile', models.CharField(max_length=14, unique=True)),
                ('cv', models.FileField(blank=True, null=True, upload_to='CV')),
                ('about', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='DP')),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Education')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Position')),
            ],
        ),
    ]