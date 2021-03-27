# Generated by Django 3.1.6 on 2021-03-27 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audiobook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, default='draft', max_length=100, verbose_name='Title')),
                ('author_title', models.CharField(db_index=True, default='draft', max_length=100, verbose_name='Author_Title')),
                ('narrator', models.CharField(db_index=True, default='draft', max_length=100, verbose_name='Narrator')),
                ('audiobook_durations', models.IntegerField(blank=True, null=True, verbose_name='Audiobook_Durations')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Datetime')),
            ],
            options={
                'db_table': 'audiobook',
            },
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('podcast_name', models.CharField(db_index=True, default='draft', max_length=100, verbose_name='Podcast_Name')),
                ('podcast_durations', models.IntegerField(blank=True, null=True, verbose_name='Podcast_Durations')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Datetime')),
                ('host', models.CharField(db_index=True, default='draft', max_length=100, verbose_name='Host')),
                ('participants', models.CharField(db_index=True, default='draft', max_length=100, verbose_name='Participants')),
            ],
            options={
                'db_table': 'podcast',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(db_index=True, default='draft', max_length=100, verbose_name='Song_Name')),
                ('song_durations', models.IntegerField(blank=True, null=True, verbose_name='Song_Durations')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Datetime')),
            ],
            options={
                'db_table': 'song',
            },
        ),
        migrations.CreateModel(
            name='AudioFileType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('song', 'Song'), ('podcast', 'Podcast'), ('audiobook', 'Audiobook')], db_index=True, default='draft', max_length=100, verbose_name='Type')),
                ('audiobook', models.ManyToManyField(to='api.Audiobook')),
                ('podcast', models.ManyToManyField(to='api.Podcast')),
                ('song', models.ManyToManyField(to='api.Song')),
            ],
            options={
                'db_table': 'audio_file_type',
            },
        ),
    ]