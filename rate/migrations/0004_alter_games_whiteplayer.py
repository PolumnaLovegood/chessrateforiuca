# Generated by Django 4.0.3 on 2022-04-15 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0003_profile_rd_alter_games_whiteplayer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='whitePlayer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='rate.profile'),
        ),
    ]
