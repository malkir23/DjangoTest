# Generated by Django 2.1.5 on 2019-01-17 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoTest', '0002_auto_20190117_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='category',
            field=models.CharField(choices=[('TO DO', 'TO DO'), ('In progress', 'In progress'), ('Done', 'Done')], default='TO DO', max_length=10),
        ),
    ]