# Generated by Django 3.2.7 on 2022-01-21 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20220116_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('book_author', models.CharField(max_length=50)),
                ('book_edition', models.IntegerField()),
                ('book_price', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Meet',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
