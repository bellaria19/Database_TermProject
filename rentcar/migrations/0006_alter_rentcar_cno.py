# Generated by Django 4.2.1 on 2023-05-29 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rentcar', '0005_alter_rentcar_datedue_alter_rentcar_daterented'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentcar',
            name='cno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]