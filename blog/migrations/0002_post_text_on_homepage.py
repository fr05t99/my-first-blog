# Generated by Django 2.0.10 on 2019-01-22 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text_on_homepage',
            field=models.CharField(default='S', max_length=200, null=True),
        ),
    ]