# Generated by Django 2.0.6 on 2018-06-04 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goheys.Topic'),
        ),
    ]
