# Generated by Django 4.1.7 on 2023-04-12 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_comment_comment_blog_app_co_created_559965_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='aaa@bbb.com', max_length=254),
        ),
    ]
