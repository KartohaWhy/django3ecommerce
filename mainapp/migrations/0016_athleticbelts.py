# Generated by Django 3.2.3 on 2021-11-07 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_auto_20200730_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='AthleticBelts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('color', models.CharField(max_length=255, verbose_name='Цвет пояса')),
                ('size', models.CharField(max_length=255, verbose_name='Размер пояса')),
                ('layers', models.CharField(max_length=255, verbose_name='Количество слоёв')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
