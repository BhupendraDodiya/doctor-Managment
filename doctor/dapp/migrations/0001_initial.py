# Generated by Django 4.1.5 on 2023-02-27 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Degree', models.CharField(max_length=100)),
                ('Contact', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='docimage/')),
                ('Category', models.CharField(max_length=100)),
            ],
        ),
    ]