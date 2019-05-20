# Generated by Django 2.2.1 on 2019-05-20 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_medida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80)),
                ('marca', models.CharField(max_length=80)),
                ('tipo', models.CharField(max_length=80)),
                ('peso', models.FloatField()),
            ],
        ),
    ]
