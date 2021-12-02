# Generated by Django 3.2.6 on 2021-12-02 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_remove_standing_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeasonStanding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveIntegerField(verbose_name='Total points')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standing', to='main.season', verbose_name='season')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standing', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'standing',
                'verbose_name_plural': 'standings',
            },
        ),
        migrations.DeleteModel(
            name='Standing',
        ),
    ]