# Generated by Django 4.0.2 on 2022-03-06 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0003_topic_media'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadTopics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_topic_name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('media', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='topic',
            name='media',
        ),
    ]