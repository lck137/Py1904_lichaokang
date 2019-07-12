# Generated by Django 2.2.1 on 2019-07-05 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('U_name', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=20)),
                ('U_account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.Account')),
            ],
        ),
    ]
