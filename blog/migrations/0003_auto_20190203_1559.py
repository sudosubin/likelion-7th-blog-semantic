# Generated by Django 2.1.5 on 2019-02-03 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190203_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(verbose_name='발행일'),
        ),
    ]