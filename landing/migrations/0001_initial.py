# Generated by Django 3.1.5 on 2021-01-24 04:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('weekly_laundry_loads', models.IntegerField()),
                ('daily_bathroom_trips', models.IntegerField()),
                ('weekly_showers', models.IntegerField()),
                ('shower_times', models.IntegerField()),
                ('weekly_baths', models.IntegerField()),
                ('weekly_dishes', models.IntegerField()),
                ('weekly_sprinkler', models.IntegerField()),
                ('shower_head', models.CharField(choices=[('Normal Shower Head', 'Normal Shower Head'), ('Efficient Shower Head', 'Efficient Shower Head')], max_length=30)),
                ('washer_type', models.CharField(choices=[('Top Load Washer', 'Top Load Washer'), ('Front Load Washer', 'Front Load Washer')], max_length=30)),
                ('swimming_pool', models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'), ("I Don't Have A Pool", "I Don't Have A Pool")], max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]