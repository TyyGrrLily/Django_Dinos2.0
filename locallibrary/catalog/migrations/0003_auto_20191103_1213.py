# Generated by Django 2.0.5 on 2019-11-03 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_animals'),
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a environment (e.g. Dessert)', max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='MyModelName',
        ),
        migrations.RemoveField(
            model_name='animals',
            name='description',
        ),
        migrations.RemoveField(
            model_name='animals',
            name='name',
        ),
        migrations.AddField(
            model_name='animals',
            name='species',
            field=models.CharField(default='unknown', max_length=200),
        ),
        migrations.AddField(
            model_name='animals',
            name='environment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Environment'),
        ),
    ]