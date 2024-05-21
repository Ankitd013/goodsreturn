# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2019-03-02 08:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerservice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csr_no', models.CharField(max_length=255)),
                ('emp_no', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=255)),
                ('emp_password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='employeecustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='complain',
            name='grn',
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AddField(
            model_name='employeecustomer',
            name='csr_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Complain'),
        ),
    ]
