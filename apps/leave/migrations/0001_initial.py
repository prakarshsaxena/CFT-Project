<<<<<<< HEAD
# Generated by Django 2.0.6 on 2018-06-12 04:52
=======
# Generated by Django 2.0.6 on 2018-06-11 05:57
>>>>>>> 03a778f3753bb395b5cd6b8ef98084e3087dd3c7

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pl', models.IntegerField(default=None)),
                ('cl', models.IntegerField(default=None)),
                ('half_day', models.IntegerField(default=None)),
                ('comp_off', models.IntegerField(default=None)),
            ],
        ),
    ]
