# Generated by Django 2.1.1 on 2018-12-10 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sells', '0005_auto_20181204_1325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='product',
            name='stuid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User', to='login_res.User'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tel',
            field=models.CharField(db_index=True, max_length=11),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
