# Generated by Django 4.1.1 on 2022-09-16 20:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_reminder'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
    ]