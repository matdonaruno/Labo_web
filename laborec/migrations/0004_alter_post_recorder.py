# Generated by Django 4.1.5 on 2023-02-04 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laborec', '0003_post_recorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='recorder',
            field=models.CharField(default='admin', max_length=20),
        ),
    ]
