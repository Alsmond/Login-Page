# Generated by Django 4.2a1 on 2023-02-09 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='login',
            old_name='lname',
            new_name='Lname',
        ),
        migrations.RenameField(
            model_name='login',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='login',
            old_name='password',
            new_name='Password',
        ),
    ]
