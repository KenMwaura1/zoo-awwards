# Generated by Django 3.2.8 on 2021-10-26 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('z_awwards', '0009_auto_20211026_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproject',
            name='photo',
            field=models.ImageField(blank=True, default='images/user_post/default.jpg', null=True, upload_to='images/user_post/'),
        ),
    ]
