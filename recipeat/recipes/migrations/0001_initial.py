# Generated by Django 5.1.1 on 2024-09-20 16:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('yields', models.CharField(max_length=255)),
                ('total_time', models.IntegerField()),
                ('image', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Instructions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.IntegerField()),
                ('text', models.TextField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('preparation', models.CharField(max_length=255)),
                ('purpose', models.CharField(max_length=255)),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=7)),
                ('quantity_max', models.DecimalField(decimal_places=3, max_digits=7)),
                ('sentence', models.TextField()),
                ('size', models.CharField(max_length=255)),
                ('unit', models.CharField(max_length=255)),
                ('unit_text', models.CharField(max_length=255)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
            ],
        ),
    ]
