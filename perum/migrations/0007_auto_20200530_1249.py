# Generated by Django 3.0.6 on 2020-05-30 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perum', '0006_akun'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelanggan',
            name='nama',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='perum.Akun'),
        ),
    ]
