# Generated by Django 3.0.5 on 2020-04-11 03:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exhaust_port', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defencetower',
            name='target',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='towers', to='exhaust_port.XWing'),
        ),
        migrations.AlterField(
            model_name='xwing',
            name='pilot',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wing', to=settings.AUTH_USER_MODEL),
        ),
    ]
