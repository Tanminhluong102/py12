# Generated by Django 3.2.8 on 2021-10-31 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_rename_deatil_view_new_detail_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=2000)),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('subject', models.CharField(max_length=200)),
            ],
        ),
    ]