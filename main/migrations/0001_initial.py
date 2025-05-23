# Generated by Django 5.0.3 on 2024-07-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request_a_Demo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=250)),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=250)),
                ('subject', models.CharField(max_length=500)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]
