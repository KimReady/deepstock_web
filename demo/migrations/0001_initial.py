# Generated by Django 2.2.7 on 2019-11-27 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=6)),
                ('price', models.IntegerField()),
                ('biz_type', models.CharField(max_length=20)),
                ('market_type', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name': '종목',
                'verbose_name_plural': '종목 리스트',
                'ordering': ['-price'],
            },
        ),
        migrations.CreateModel(
            name='PredictedPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('now', models.IntegerField()),
                ('tomorrow', models.IntegerField()),
                ('after_a_month', models.IntegerField()),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='demo.Company')),
            ],
            options={
                'verbose_name': '종목 주가 예측 리스트',
                'ordering': ['-now'],
            },
        ),
    ]