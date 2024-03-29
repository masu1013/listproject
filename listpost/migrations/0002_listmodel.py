# Generated by Django 3.1.7 on 2021-04-15 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listpost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=12)),
                ('units', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5以上'), ('none', '無')], max_length=50)),
                ('company', models.CharField(choices=[('docomo', 'docomo'), ('au', 'au'), ('softbank', 'softbank'), ('UQ', 'UQ'), ('Ymobile', 'Ymobile'), ('none', '無')], max_length=50)),
                ('bb', models.CharField(choices=[('docomo', 'docomo光'), ('au', 'auひかり・固定代替'), ('softbank', 'softbank光・Air'), ('nifty', 'nifty光'), ('NURO', 'NURO光'), ('other', 'その他'), ('none', '無')], max_length=50)),
                ('layaway', models.CharField(choices=[('OK', '済'), ('none', '未')], max_length=50)),
                ('remarks', models.TextField(max_length=200)),
                ('postdate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
