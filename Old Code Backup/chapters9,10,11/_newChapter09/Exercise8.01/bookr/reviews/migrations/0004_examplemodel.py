# Generated by Django 3.0 on 2020-01-23 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20191227_0751'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_field', models.ImageField(upload_to='images/')),
                ('file_field', models.FileField(upload_to='files/')),
            ],
        ),
    ]
