# Generated by Django 3.2.9 on 2022-02-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blogcomment_sno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='sno',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
