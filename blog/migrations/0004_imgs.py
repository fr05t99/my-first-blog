# Generated by Django 2.0.10 on 2019-02-03 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190122_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imgs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
    ]
