# Generated by Django 4.2.10 on 2024-02-11 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='tags',
            field=models.ManyToManyField(null=True, related_name='tag', to='dashboard.tag'),
        ),
    ]
