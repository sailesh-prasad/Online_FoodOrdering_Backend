# Generated by Django 5.1.4 on 2024-12-24 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0017_delete_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='place',
            field=models.CharField(max_length=50),
        ),
    ]
