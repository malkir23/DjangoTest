# Generated by Django 2.1.5 on 2019-01-17 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoTest', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'verbose_name': 'Work', 'verbose_name_plural': 'Works'},
        ),
        migrations.AlterField(
            model_name='board',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name Works'),
        ),
    ]
