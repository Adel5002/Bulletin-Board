# Generated by Django 4.2 on 2023-05-05 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MMORPGapp', '0003_post_datecreation'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='accept_comment',
            field=models.BooleanField(default=False),
        ),
    ]
