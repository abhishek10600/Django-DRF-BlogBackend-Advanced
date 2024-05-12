# Generated by Django 5.0.4 on 2024-05-04 07:56

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_remove_blog_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('created_at', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='description',
            new_name='blog_description',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='name',
            new_name='blog_title',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='blog_app.category'),
        ),
    ]
