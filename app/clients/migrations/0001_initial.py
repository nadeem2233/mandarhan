# Generated by Django 2.2.7 on 2019-11-16 11:33

import app.clients.uploads
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=160, null=True, verbose_name='last name')),
                ('first_name', models.CharField(max_length=160, verbose_name='first name')),
                ('second_name', models.CharField(blank=True, max_length=160, null=True, verbose_name='second name')),
                ('additional_info', models.CharField(blank=True, max_length=255, null=True, verbose_name='additional info')),
                ('phone', models.CharField(blank=True, max_length=32, null=True, verbose_name='phone')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='email')),
                ('address', models.TextField(blank=True, null=True, verbose_name='address')),
                ('in_vip', models.BooleanField(default=False, verbose_name='in VIP list')),
                ('in_blacklist', models.BooleanField(default=False, verbose_name='in blacklist')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='comment')),
                ('is_foreigner', models.BooleanField(default=False, verbose_name='is foreigner?')),
                ('sex', models.CharField(blank=True, choices=[('M', 'male'), ('F', 'female')], max_length=1, verbose_name='sex')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='birthday')),
                ('identification_doc', models.CharField(blank=True, max_length=160, null=True, verbose_name='identification document name')),
                ('doc_serial', models.CharField(blank=True, max_length=30, null=True, verbose_name='document serial')),
                ('doc_number', models.CharField(blank=True, max_length=160, null=True, verbose_name='document number')),
                ('doc_date', models.DateField(blank=True, null=True, verbose_name='document date is issue')),
                ('doc_issued_by', models.CharField(blank=True, max_length=255, null=True, verbose_name='document issued by')),
                ('added_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='client added at')),
            ],
            options={
                'verbose_name': 'client',
                'verbose_name_plural': 'clients',
                'ordering': ['-added_at'],
            },
        ),
        migrations.CreateModel(
            name='ClientPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(editable=False, max_length=255)),
                ('photo', models.ImageField(upload_to=app.clients.uploads.upload_client_photo, verbose_name='client photo')),
                ('thumbnail', models.ImageField(editable=False, upload_to=app.clients.uploads.upload_thumbnail, verbose_name='photo preview')),
                ('added_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='photo added at')),
                ('my_order', models.PositiveSmallIntegerField(default=0, verbose_name='order')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_clients.Client', verbose_name='client')),
            ],
            options={
                'verbose_name': 'client photo',
                'verbose_name_plural': 'client photos',
                'ordering': ['my_order'],
            },
        ),
    ]
