# Generated by Django 4.0.2 on 2022-02-22 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exp_v1', '0002_rename_name_user_fullname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exp_v1.user'),
        ),
    ]
