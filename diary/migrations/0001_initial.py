# Generated by Django 3.1.4 on 2021-01-31 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='タイトル')),
                ('content', models.TextField(blank=True, null=True, verbose_name='本文')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真１')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真２')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真３')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.customuser', verbose_name='ユーザー')),
            ],
            options={
                'verbose_name': 'Diary',
            },
        ),
    ]
