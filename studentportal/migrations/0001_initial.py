# Generated by Django 5.2.1 on 2025-06-27 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('class_name', models.CharField(max_length=50)),
                ('entry_class', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveBigIntegerField()),
                ('type', models.CharField(choices=[('bot', 'Beginning of Term'), ('mot', 'Mid Term'), ('eot', 'End of Term'), ('mock', 'Mock examination'), ('test', 'Test')], max_length=10)),
            ],
        ),
    ]
