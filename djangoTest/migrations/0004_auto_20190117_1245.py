# Generated by Django 2.1.5 on 2019-01-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoTest', '0003_auto_20190117_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='category',
            field=models.CharField(choices=[('TO DO', 'TO DO'), ('In progress', 'In progress'), ('Done', 'Done')], default='TO DO', max_length=15),
        ),
    ]
