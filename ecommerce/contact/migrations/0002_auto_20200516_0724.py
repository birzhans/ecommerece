# Generated by Django 2.2.6 on 2020-05-16 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='some@email.com', max_length=254),
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default='No subject', max_length=50),
        ),
    ]
