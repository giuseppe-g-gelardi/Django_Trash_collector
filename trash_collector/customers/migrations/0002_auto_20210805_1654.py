# Generated by Django 3.2.5 on 2021-08-05 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customer',
            name='one_time_pickup',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='suspend_end',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='suspend_start',
            field=models.DateField(null=True),
        ),
        migrations.CreateModel(
            name='BudgetInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_budget', models.IntegerField(default=0)),
                ('expenses', models.IntegerField(default=0)),
                ('usdr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.accountinfo')),
            ],
        ),
    ]