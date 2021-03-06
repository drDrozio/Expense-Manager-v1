# Generated by Django 4.0.2 on 2022-02-22 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp_v1', '0003_alter_expense_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('Electricity', 'Electricity'), ('Food', 'Food'), ('Gifts', 'Gifts'), ('Groceries', 'Groceries'), ('Miscellaneous', 'Miscellaneous'), ('Recreations', 'Recreations'), ('Rent', 'Rent'), ('Subscriptions', 'Subscriptions'), ('Transportation', 'Transportation'), ('Travel', 'Travel'), ('Water', 'Water')], max_length=255),
        ),
    ]
