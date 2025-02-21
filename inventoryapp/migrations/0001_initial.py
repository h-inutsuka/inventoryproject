# Generated by Django 4.0 on 2025-01-31 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventoryapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(default='default.jpg', upload_to='products/')),
                ('stock', models.PositiveSmallIntegerField(verbose_name='在庫数')),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('explanation', models.TextField(max_length=300, verbose_name='説明文')),
                ('price', models.PositiveIntegerField(verbose_name='値段')),
                ('inventor', models.PositiveSmallIntegerField(verbose_name='在庫数')),
                ('category', models.CharField(choices=[('pants', 'ズボン')], max_length=20, verbose_name='カテゴリ')),
                ('situation', models.TextField(verbose_name='状態')),
                ('image1', models.ImageField(upload_to='photos', verbose_name='イメージ１')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='イメージ２')),
            ],
        ),
    ]
