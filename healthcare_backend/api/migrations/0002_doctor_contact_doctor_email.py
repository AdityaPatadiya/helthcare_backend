# Generated by Django 5.2.2 on 2025-06-06 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='contact',
            field=models.CharField(default=1234567890, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='email',
            field=models.EmailField(default='unknown@example.com', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
