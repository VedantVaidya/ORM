# Generated by Django 4.1.2 on 2022-11-02 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sallery', models.IntegerField()),
                ('account_number', models.IntegerField()),
                ('pf', models.IntegerField()),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.employee')),
            ],
        ),
    ]
