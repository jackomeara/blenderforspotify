# Generated by Django 3.2.9 on 2021-12-19 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blender', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='criteriamodel',
            name='name',
            field=models.CharField(default='NAME', max_length=50),
            preserve_default=False,
        ),
    ]
