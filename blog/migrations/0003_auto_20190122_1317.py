# Generated by Django 2.0.10 on 2019-01-22 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_text_on_homepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text_on_homepage',
            field=models.CharField(default='Click on Post title to view post', max_length=200, null=True),
        ),
    ]
