# Generated by Django 4.1 on 2022-08-27 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_rename_todo_category_category_rename_todo_item_todo'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='todo_1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='todo_2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='todo_3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='todo_4',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='todo_5',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
