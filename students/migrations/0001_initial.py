# Generated by Django 5.0.1 on 2024-01-29 08:51

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
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=14)),
                ('university', models.CharField(choices=[('PTU', 'Pharmaceutical Technical University'), ('TEAM', 'TEAM University'), ('TSPU', 'Tashkent State Pedagogical University'), ('WIUT', 'Westminster International University in Tashkent')], default='WIUT', max_length=4)),
                ('type', models.CharField(choices=[('BS', 'Bachelors'), ('PG', 'Post Graduate')], default='BS', max_length=4)),
                ('fee', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]