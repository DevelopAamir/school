# Generated by Django 4.1.7 on 2023-02-18 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satyanarayan', '0003_alter_facilitie_title_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facilitie',
            name='img',
            field=models.ImageField(upload_to='thumbnails'),
        ),
    ]
