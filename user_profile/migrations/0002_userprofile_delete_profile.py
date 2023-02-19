# Generated by Django 4.1.5 on 2023-02-19 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github', models.CharField(blank=True, max_length=200, null=True)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('languages', models.CharField(blank=True, max_length=250, null=True)),
                ('bio', models.CharField(blank=True, max_length=1000, null=True)),
                ('strengths', models.CharField(blank=True, max_length=80, null=True)),
                ('weaknesses', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
