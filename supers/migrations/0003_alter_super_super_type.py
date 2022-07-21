# Generated by Django 4.0.6 on 2022-07-21 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0001_initial'),
        ('supers', '0002_super_super_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='super',
            name='super_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='super_types.supertype'),
            preserve_default=False,
        ),
    ]
