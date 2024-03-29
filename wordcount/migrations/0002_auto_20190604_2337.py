# Generated by Django 2.1.7 on 2019-06-04 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordcount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('subject', models.CharField(max_length=20)),
                ('body', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(verbose_name='마감기한'),
        ),
    ]
