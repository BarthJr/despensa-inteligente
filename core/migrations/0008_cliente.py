# Generated by Django 2.2.1 on 2019-05-24 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_produtodespensa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('login', models.CharField(max_length=120)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
    ]