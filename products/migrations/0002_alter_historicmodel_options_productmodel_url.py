# Generated by Django 4.0 on 2021-12-16 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicmodel',
            options={'ordering': ['-date'], 'verbose_name': 'Historic', 'verbose_name_plural': 'Histories'},
        ),
        migrations.AddField(
            model_name='productmodel',
            name='url',
            field=models.URLField(default='https://www.amazon.com.br/', max_length=300),
        ),
    ]
