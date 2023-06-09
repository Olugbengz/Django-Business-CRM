# Generated by Django 4.1.7 on 2023-04-02 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buz_website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('birttday', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=60)),
                ('zipcode', models.CharField(max_length=60)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
