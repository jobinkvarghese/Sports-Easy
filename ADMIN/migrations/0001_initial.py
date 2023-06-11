# Generated by Django 4.2.2 on 2023-06-10 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='itemtable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=25)),
                ('itemprice', models.IntegerField()),
                ('itemdecription', models.TextField()),
                ('picture', models.FileField(upload_to='images')),
            ],
        ),
    ]
