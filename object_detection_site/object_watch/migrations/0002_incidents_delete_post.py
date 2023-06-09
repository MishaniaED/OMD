# Generated by Django 4.1.7 on 2023-03-31 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object_watch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incidents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Event Name')),
                ('event_date', models.DateTimeField(verbose_name='Event Date')),
                ('location', models.CharField(max_length=120)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
