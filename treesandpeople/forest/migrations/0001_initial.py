# Generated by Django 2.0.4 on 2018-04-07 11:45

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CultureSpecies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratio', models.FloatField(help_text='fraction, monoculture equivalent')),
                ('culture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forest.Culture')),
            ],
        ),
        migrations.CreateModel(
            name='Forest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ForestCulture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.FloatField()),
                ('culture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forest.Culture')),
                ('forest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forest.Forest')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('labour_price', models.FloatField(help_text='€ per hour')),
                ('forests', models.ManyToManyField(to='forest.Forest')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('plants_per_area', models.FloatField(help_text='per square meter')),
                ('labour_per_plant', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(help_text='hours per year'), size=None)),
                ('costs_per_plant', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(help_text='€ per year, including initial costs'), size=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpeciesProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yield_per_plant', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(help_text='metric tons per year'), size=None)),
                ('labour_per_plant', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(help_text='hours per year'), size=None)),
                ('costs_per_plant', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(help_text='€ per year'), size=None)),
                ('price', models.FloatField(help_text='sales price per metric ton')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forest.Product')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forest.Species')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.AddField(
            model_name='species',
            name='products',
            field=models.ManyToManyField(through='forest.SpeciesProduct', to='forest.Product'),
        ),
        migrations.AddField(
            model_name='forest',
            name='cultures',
            field=models.ManyToManyField(through='forest.ForestCulture', to='forest.Culture'),
        ),
        migrations.AddField(
            model_name='culturespecies',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forest.Species'),
        ),
        migrations.AddField(
            model_name='culture',
            name='species',
            field=models.ManyToManyField(through='forest.CultureSpecies', to='forest.Species'),
        ),
    ]
