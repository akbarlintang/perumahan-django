# Generated by Django 3.0.6 on 2020-05-30 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perum', '0007_auto_20200530_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelanggan',
            name='nama',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Akun',
        ),
    ]
