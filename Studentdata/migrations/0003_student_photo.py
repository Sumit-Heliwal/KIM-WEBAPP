# Generated by Django 4.0.6 on 2022-11-16 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Studentdata', '0002_hostel_floor'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Photo',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
