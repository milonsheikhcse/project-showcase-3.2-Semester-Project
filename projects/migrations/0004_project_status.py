# Generated by Django 3.1 on 2020-10-27 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_project_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(default='processing', max_length=255),
        ),
    ]